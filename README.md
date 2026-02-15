![APK-Hunter Banner](banner.png)

# 🔍 APKHUNTER – Android Security Analysis Tool

<p align="center">
  <img src="./banner.png" alt="APKHUNTER Banner" width="90%" />
</p>

> **APKHUNTER** is a comprehensive static analysis tool for Android applications, designed to detect security vulnerabilities based on the **OWASP Mobile Top 10**.

---

## 📖 Table of Contents

- [Features](#-features)
- [OWASP Coverage](#-owasp-mobile-top-10-coverage)
- [Installation](#-installation)
- [Usage](#-usage)
- [Reports](#-reports)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- 🔍 Static APK analysis using JADX
- 📱 AndroidManifest inspection
- 🔐 Hardcoded secret detection
- 🌐 Insecure network communication scan
- 🛡️ Code tampering & reverse engineering detection
- 📊 Risk scoring engine
- 📄 Multiple report formats (JSON, PDF, HTML, TXT)
- ⚙️ CLI-based interface

---

## 📌 OWASP Mobile Top 10 Coverage

| ID  | Category                     | Support |
|-----|------------------------------|---------|
| M1  | Improper Platform Usage      | Partial |
| M2  | Insecure Data Storage         | ✅ Yes  |
| M3  | Insecure Communication       | ✅ Yes  |
| M4  | Insecure Authentication      | ✅ Yes  |
| M5  | Insufficient Cryptography    | ✅ Yes  |
| M6  | Broken Authorization         | ✅ Yes  |
| M7  | Client Code Quality          | Partial |
| M8  | Code Tampering               | ✅ Yes  |
| M9  | Reverse Engineering          | ✅ Yes  |
| M10 | Extraneous Functionality     | ✅ Yes  |

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/SagaRXD-hue/APKHUNTER.git
cd APKHUNTER
```

### 2️⃣ Activate Virtual Environment

> A virtual environment is already included.

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / macOS
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Basic Scan

```bash
python APKHUNTER.py -apk sample.apk
```

### Generate JSON Report

```bash
python APKHUNTER.py -apk sample.apk -report json -o reports/
```

### Generate PDF Report

```bash
python APKHUNTER.py -apk sample.apk -report pdf -o report.pdf
```

### Ignore Virtual Environment Check

```bash
python APKHUNTER.py -apk sample.apk --ignore_virtualenv
```

---

## ⚙️ Command-Line Options

```text
usage: APKHUNTER.py [-h] -apk APK [-v]
                    [-source_code_path APK]
                    [-report {json,pdf,html,txt}]
                    [-o OUTPUT]
                    [--ignore_virtualenv]
                    [-l LOGLEVEL]
```

| Option | Description |
|--------|-------------|
| -apk | Path to APK file |
| -v | Show version |
| -source_code_path | Use pre-extracted source |
| -report | Report format |
| -o | Output path |
| --ignore_virtualenv | Skip venv check |
| -l | Logging level |

---

## 📄 Reports

APKHUNTER supports multiple report formats:

- 📘 **JSON** – Machine-readable output
- 📕 **PDF** – Printable security report
- 🌐 **HTML** – Interactive report
- 📃 **TXT** – Plain text summary

Example output:

```bash
reports/report_file.json
reports/report_file.pdf
```

---

## 📁 Project Structure

```text
APKHUNTER/
│
├── analyzer/           # Reverse engineering checks
├── static_tools/       # OWASP checkers
├── report_gen/         # Report generators
├── app_source/         # Decompiled APK source
├── reports/            # Generated reports
├── venv/               # Virtual environment
├── APKHUNTER.py        # Main entry point
└── requirements.txt
```

---

## ⭐ Acknowledgements

- OWASP Mobile Top 10
- JADX Decompiler
- Open-source security community

---

<p align="center">
  Developed by <b>Team Diamond</b> 💎
</p>

