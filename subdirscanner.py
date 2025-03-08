import os
import requests
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from sublist3r import sublist3r
import validators
import logging

# قائمة البروتوكولات المعروفة
PROTOCOLS = [
    "http", "https", "ftp", "sftp", "smb", "ldap", "rdp", "ssh"
]

# إعداد تسجيل الأحداث (logging)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# دعم جميع البروتوكولات وبروكسي
def check_directories(subdomain, wordlist, proxy=None, timeout=5):
    found_directories = []
    try:
        with open(wordlist, 'r') as file:
            for line in file:
                directory = line.strip()
                if not directory:
                    continue  # تجاهل السطور الفارغة
                for protocol in PROTOCOLS:
                    url = f"{protocol}://{subdomain}/{directory}"
                    try:
                        response = requests.get(url, proxies=proxy, timeout=timeout)
                        if response.status_code == 200:
                            logging.info(f"[+] Found: {url}")
                            found_directories.append(url)
                            break  # إذا تم العثور على المسار، توقف عن البحث
                    except requests.exceptions.RequestException:
                        continue
    except FileNotFoundError:
        logging.error(f"[-] Wordlist file '{wordlist}' not found.")
    except Exception as e:
        logging.error(f"[-] Error checking directories for {subdomain}: {e}")
    return found_directories

# حفظ النتائج
def save_results(domain, subdomain, found_directories):
    results_dir = os.path.abspath(domain)
    os.makedirs(results_dir, exist_ok=True)
    result_file = os.path.join(results_dir, f"{subdomain}.txt")
    try:
        with open(result_file, 'w') as file:
            for directory in found_directories:
                file.write(f"{directory}\n")
        logging.info(f"[+] Results saved to {result_file}")
    except Exception as e:
        logging.error(f"[-] Failed to save results for {subdomain}: {e}")

# الوظيفة الرئيسية لفحص الدايركتريز باستخدام Threading
def threaded_check(subdomain, wordlist, proxy, timeout, results):
    try:
        found_directories = check_directories(subdomain, wordlist, proxy, timeout)
        results[subdomain] = found_directories
    except Exception as e:
        logging.error(f"[-] Error processing {subdomain}: {e}")

# الوظيفة الرئيسية
def main():
    show_banner()

    # إدخال المستخدم
    domain = input("Enter the domain: ").strip()
    if not validators.domain(domain):
        logging.error("[-] Invalid domain entered.")
        return

    wordlist = input("Enter the path to the wordlist file: ").strip()
    if not os.path.isfile(wordlist):
        logging.error(f"[-] Wordlist file '{wordlist}' not found.")
        return

    threads_count = int(input("Enter number of threads (e.g., 10): "))
    timeout = int(input("Enter request timeout (seconds): "))

    use_proxy = input("Use proxy? (y/n): ").lower() == 'y'
    proxy = {}
    if use_proxy:
        http_proxy = input("Enter HTTP proxy (e.g., http://proxy:port): ").strip()
        https_proxy = input("Enter HTTPS proxy (e.g., http://proxy:port): ").strip()
        proxy = {
            "http": http_proxy,
            "https": https_proxy
        }

    # استخراج السابدومينات
    logging.info(f"[+] Enumerating subdomains for {domain}...")
    subdomains = sublist3r.main(domain, 40, None, ports=None, silent=False, verbose=True, enable_bruteforce=False, engines=None)
    if not subdomains:
        logging.error(f"[-] No subdomains found for {domain}.")
        return
    logging.info(f"[+] Found {len(subdomains)} subdomains: {', '.join(subdomains)}")

    # فحص الدايركتريز باستخدام Threading
    results = {}
    logging.info(f"[+] Starting directory scan with {threads_count} threads...")
    with ThreadPoolExecutor(max_workers=threads_count) as executor:
        futures = {executor.submit(threaded_check, subdomain, wordlist, proxy, timeout, results): subdomain for subdomain in subdomains}

        for future in as_completed(futures):
            subdomain = futures[future]
            try:
                future.result()
            except Exception as e:
                logging.error(f"[-] Error processing {subdomain}: {e}")

    # حفظ النتائج
    logging.info("[+] Saving results...")
    for subdomain, found_directories in results.items():
        save_results(domain, subdomain, found_directories)

    logging.info("[+] Scan completed.")

# عرض الشعار
def show_banner():
    print("""
███████╗██╗   ██╗██████╗ ██████╗ ██╗██████╗       ███████╗
██╔════╝██║   ██║██╔══██╗██╔══██╗██║██╔══██╗      ██╔════╝
███████╗██║   ██║██████╔╝██║  ██║██║██████╔╝█████╗███████╗
╚════██║██║   ██║██╔══██╗██║  ██║██║██╔══██╗╚════╝╚════██║
███████║╚██████╔╝██████╔╝██████╔╝██║██║  ██║      ███████║
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝      ╚══════╝
========================================================
    🐦 Twitter: @vulnquest    
    🐙 GitHub: github.com/vulnquest58   
    💼 LinkedIn: linkedin.com/company/vulnquest
    💬 Discord: discord.gg/vulnquest
    🌐 Website: vulnquest.com
========================================================
    """)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("\n[+] Scan interrupted by user.")
