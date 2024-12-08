# 🌐 Domain Grabber Tool

<p align="center">
  <img src="https://github.com/user-attachments/assets/dfe19bab-1a86-4138-a953-ec29d5e21b5c" alt="Domain Grabber Banner" width="600">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue.svg">
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
  <img src="https://img.shields.io/badge/Version-1.0.0-red.svg">
</p>

A powerful and efficient domain grabbing tool written in Python. This tool helps you discover domains with specific extensions through Google search results.

## ✨ Features

- 🚀 Multi-threaded domain discovery
- 🔄 Random User-Agent rotation
- ⏱️ Configurable request delays
- ✅ Domain validation
- 📊 Detailed progress reporting
- 💾 Organized output format
- ⚡ High performance and reliability

## 🛠️ Installation
```bash
~$ git clone https://github.com/JagungBakarEnak07/Domain-Grabber.git
~$ cd Domain-Grabber
~$ pip3 install -r requirements.txt
```

## 📚 Usage

Basic command structure:
```bash
python3 grabber.py -e [EXTENSION] -p [PAGES] -t [THREADS] -o [OUTPUT]
```

### Examples

1. Basic Usage:
```bash
python3 grabber.py -e go.id -o government.txt
```
2. Advanced Usage with More Pages:
```bash
python3 grabber.py -e ac.id -p 20 -t 10 -o universities.txt
```
3. With Delay Between Requests:
```bash
python3 grabber.py -e co.id -p 15 -t 5 -d 1.0 -o companies.txt
```


### 📋 Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `-e, --extension` | Domain extension to search | Required |
| `-o, --output` | Output file path | domains.txt |
| `-p, --pages` | Number of pages to search | 10 |
| `-t, --threads` | Number of threads to use | 5 |
| `-d, --delay` | Delay between requests (seconds) | 0 |
| `--timeout` | Request timeout (seconds) | 10 |

## 📊 Output Example
```text
[2024-12-08 03:24:22] Starting domain grabber for .go.id
[2024-12-08 03:24:22] Using 5 threads and 10 pages
[2024-12-08 03:24:23] Found 8 domains on page 1
[2024-12-08 03:24:24] Found 6 domains on page 2
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/JagungBakarEnak07/Domain-Grabber/issues).

## 🌟 Show your support

Give a ⭐️ if this project helped you!

## 📞 Contact

- GitHub: [@JagungBakarEnak07](https://github.com/JagungBakarEnak07)
- Telegram: [@JagungBakarEnak07](https://t.me/JagungBakarEnak07)

## 📜 Disclaimer

This tool is for educational purposes only. Users are responsible for complying with applicable laws and regulations.

---
<p align="center">Made with ❤️ by JagungBakarEnak07</p>
