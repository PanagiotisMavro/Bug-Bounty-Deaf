# 🐛 BugBountyDeaf

### Beginner-Friendly Bug Bounty Recon Automation Framework

BugBountyDeaf is a lightweight Python-based recon toolkit designed to help beginners understand bug bounty workflows through automation.

It focuses on **recon, endpoint discovery, and vulnerability signal gathering**, not exploitation.

---

## ❤️ Respect & Purpose

This project is created with respect for everyone learning cybersecurity, including the deaf and hard-of-hearing community.

The goal is simple:
👉 Make bug bounty recon easier to understand  
👉 Help beginners learn real security workflow step-by-step  
👉 Support learning in a clear and structured way  

Security is for everyone. Knowledge should be open, simple, and respectful.

---

## 🚀 Why this project exists

Most beginners struggle with:

* Too many tools
* No workflow structure
* No idea what to test first

This tool simplifies the process into a **single pipeline**:

> Recon → Filter → Scan → Review

---

## ⚙️ Features

* Subdomain enumeration (Subfinder / Amass)
* Live host detection (httpx)
* Wayback URL collection
* Smart endpoint filtering (juicy targets)
* Fuzzing support (ffuf)
* Template scanning (Nuclei)
* Basic vulnerability signals:

  * XSS reflection check
  * SSRF pattern testing
  * Parameter discovery

---

## 🧠 Workflow

```
Target → Subdomains → Live Hosts → URLs → Filter → Scan → Manual Testing
```

Automation handles **discovery**, YOU handle **exploitation**.

---

## 🛠 Installation

```bash
git clone https://github.com/yourname/bugbountydeaf
cd bugbountydeaf

pip install -r requirements.txt
```

Install tools:

```bash
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install github.com/ffuf/ffuf@latest
```

---

## 📌 Usage

### Full scan

```bash
python3 bugbountydeaf.py -d example.com --all
```

### Recon only

```bash
python3 bugbountydeaf.py -d example.com --recon
```

### Scan only

```bash
python3 bugbountydeaf.py -d example.com --scan
```

---

## 📂 Output

* subs.txt → discovered subdomains
* live.txt → active hosts
* urls.txt → archived endpoints
* juicy.txt → high-value endpoints
* nuclei.txt → template findings

---

## ⚠️ Disclaimer

This tool is for:

* Educational purposes
* Authorized testing only
* Bug bounty platforms like HackerOne / Bugcrowd

No exploitation or illegal use is intended.

---

## ❤️ Goal

Help beginners understand:

* how real recon works
* how bug bounty workflows are structured
* how tools connect together

---

## 🤝 Contribute

Pull requests and improvements are welcome.
