# PassCrack 🔐

**PassCrack** is a simple password cracker written in Python that supports dictionary and brute-force attacks. It's intended for ethical hacking practice, CTFs, and password security demonstrations.

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Do **NOT** use it on systems without permission.

## ✅ Features

- Dictionary-based attack
- Brute-force attack (limited)
- Hash comparison (SHA256)
- Works with custom wordlists

## 🔧 How to Use

### Dictionary Attack:
```bash
python3 cracker.py --mode dict --hashfile test/hash.txt --wordlist wordlists/common.txt
