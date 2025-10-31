<h1 align="center">⚡ Pattern Finder 🔍</h1>

<p align="center">
  <b>A multi-threaded Python tool that scans thousands of URLs for specific regex patterns</b><br>
  <b>Find and collect hidden endpoints like <span style="color:#00ffff;">something.aspx</span> or <span style="color:#39ff14;">login.php</span> in seconds.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/Threaded-YES-green.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/Regex-Powered-purple.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge">
</p>

---

## 💡 About

**Pattern Finder** is a lightweight yet powerful Python script that scans a list of URLs for specific regex-based patterns (like `.aspx`, `.php`, `.jsp`, etc.).  
It’s built for **bug bounty hunters**, **web pentesters**, and **security researchers** who need to quickly extract web file names or endpoints from live targets.

It’s fast, multi-threaded, and saves all unique matches to a text file for later analysis.

---

## 🚀 Features

✅ Multi-threaded for high performance (handles thousands of URLs)  
✅ Customizable regex pattern input  
✅ Supports custom headers (e.g., cookies or tokens)  
✅ Outputs only URLs with valid matches  
✅ Automatically saves all unique findings to a text file  
✅ Simple CLI usage – no dependencies beyond `requests`  

---

## ⚙️ Installation

Clone the repository:
```bash
git clone https://github.com/<your-username>/pattern-finder.git
cd pattern-finder
