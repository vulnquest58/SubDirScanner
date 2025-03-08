# SubDirScanner

 [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/vulnquest58/SubDirScanner/blob/main/LICENSE)[![Python Version](https://img.shields.io/badge/python-3.6%2B-brightgreen.svg) ](https://www.python.org/)[![GitHub Stars](https://img.shields.io/github/stars/yourusername/subdirscanner.svg?style=social)](https://github.com/vulnquest58/SubDirScanner)

**SubDirScanner** is a powerful Python-based tool designed for subdomain enumeration and directory scanning. It automates the process of discovering subdomains and checking for accessible directories using multithreading, making it an efficient solution for security researchers and ethical hackers.

---

## Table of Contents

1. [Features](https://github.com/vulnquest58/SubDirScanner/blob/main/README.md#features)
2. [Installation](https://github.com/vulnquest58/SubDirScanner/blob/main/README.md#installation)
3. [Usage](https://github.com/vulnquest58/SubDirScanner/blob/main/README.md#usage)
4. [Examples](https://github.com/vulnquest58/SubDirScanner/blob/main/README.md#examples)
5. [Configuration](https://github.com/vulnquest58/SubDirScanner/blob/main/README.md#configuration)
6. [Contributing](https://github.com/vulnquest58/SubDirScanner/blob/main/README.md#contributing)
7. [License](https://github.com/vulnquest58/SubDirScanner/blob/main/README.md#license)
8. [Disclaimer](https://github.com/vulnquest58/SubDirScanner/blob/main/README.md#disclaimer)

---

## Features

- **Subdomain Enumeration** : Automatically discovers subdomains for a given domain using the `sublist3r` library.
- **Directory Scanning** : Checks for accessible directories on discovered subdomains using a custom wordlist.
- **Multithreading** : Utilizes Python's `ThreadPoolExecutor` for parallel scanning, reducing execution time significantly.
- **Protocol Support** : Supports multiple protocols such as HTTP, HTTPS, FTP, SFTP, SMB, LDAP, RDP, and SSH.
- **Proxy Support** : Allows users to configure HTTP/HTTPS proxies for anonymity or bypassing restrictions.
- **Logging** : Provides detailed logs for debugging and monitoring the scanning process.
- **Result Saving** : Saves discovered directories into separate text files for each subdomain in an organized folder structure.

---

## Installation

To use **SubDirScanner** , you need to have Python 3.6 or higher installed on your system. Follow these steps to set up the tool:

1. **Clone the Repository** :

```
  git clone https://github.com/vulnquest58/SubDirScanner.git
```
```
    cd subdirscanner
```
    
2. **Install Dependencies** :
    
```
    pip install -r requirements.txt
```
    
Alternatively, install the required libraries manually:

```
    pip install requests sublist3r validators
```
    
3. **Prepare Wordlist** : Create a wordlist file (`wordlist.txt`) containing potential directory names. You can also download pre-made wordlists from sources like [SecLists](https://github.com/danielmiessler/SecLists) .
    

---

## Usage

Run the script and follow the on-screen prompts:

```
python subdirscanner.py
```

### Input Prompts:

4. **Domain** : Enter the target domain (e.g., `example.com`).
5. **Wordlist Path** : Provide the path to your wordlist file (e.g., `wordlist.txt`).
6. **Number of Threads** : Specify the number of threads for parallel scanning (e.g., `10`).
7. **Request Timeout** : Set the timeout for each request in seconds (e.g., `5`).
8. **Proxy Configuration** : Optionally configure HTTP/HTTPS proxies for anonymity.

---

## Examples

### Example 1: Basic Scan

```
python subdirscanner.py

- Enter `example.com` as the domain.
- Use `wordlist.txt` as the wordlist file.
- Set `10` threads and a timeout of `5` seconds.

```
### Example 2: Using Proxies

```
python subdirscanner.py

- Enter `example.com` as the domain.
- Use `wordlist.txt` as the wordlist file.
- Set `10` threads and a timeout of `5` seconds.
- Configure proxies:
    - HTTP Proxy: `http://proxy.example.com:8080`
    - HTTPS Proxy: `http://proxy.example.com:8080`

```
---

## Configuration

You can customize the behavior of **SubDirScanner** by modifying the following parameters:

- **Protocols** : The list of supported protocols is defined in the `PROTOCOLS` constant. You can add or remove protocols as needed.
- **Timeout** : Adjust the request timeout value to suit your needs.
- **Logging** : Logs are generated using Python's `logging` module. You can modify the log level or format in the script.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

9. Fork the repository.
10. Create a new branch for your feature or bug fix:

```
   git checkout -b feature/new-feature
```
    
11. Commit your changes:
  
```
   git commit -m "Add new feature"
```
    
12. Push your changes to your fork:
  
```
   git push origin feature/new-feature
```
    
13. Submit a pull request describing your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/vulnquest58/SubDirScanner/blob/main/LICENSE) file for more details.

---

## Disclaimer

**SubDirScanner** is intended for educational purposes and authorized security testing only. Unauthorized use of this tool to scan or attack networks without explicit permission is illegal and violates terms of service. Always ensure you have proper authorization before using this tool.

By using this tool, you agree to comply with all applicable laws and regulations.

---

## Acknowledgments

- **sublist3r** : For subdomain enumeration.
- **requests** : For handling HTTP/HTTPS requests.
- **validators** : For domain validation.
- **concurrent.futures** : For efficient multithreading.

---

If you find **SubDirScanner** useful, please consider starring the repository on GitHub! 🌟

---

**Author** : [vulnquest58]  
**Contact** : [vulnquest@gmail.com]
