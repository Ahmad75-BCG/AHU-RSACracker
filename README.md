# AHU-RSACracker 🔐

## 🇬🇧 English Description

AHU-RSACracker is an educational tool designed to demonstrate RSA cryptanalysis using factorization.

It works by recovering the private key when the prime factors of the modulus (n) are known, and then using it to decrypt RSA ciphertexts.

### ⚙️ What it does
- Recovers RSA private key (d) from known factors (p, q)
- Computes Euler’s Totient function (φ)
- Performs RSA decryption using modular exponentiation
- Converts decrypted integers back into readable data (if possible)

### 📦 Requirements
- Python 3.x
- pycryptodome
- colorama

### 🔧 Installation
```bash
pip install pycryptodome colorama
