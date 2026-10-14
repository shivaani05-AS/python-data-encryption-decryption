# python-data-encryption-decryption
A Python-based project to encrypt and decrypt text securely using cryptography techniques.
# Data Encryption and Decryption Using Python

## Project Overview
A Python-based project to encrypt and decrypt text using Fernet symmetric encryption. This project demonstrates how cryptography can help protect information from unauthorized access.

## Objectives
- To understand the basics of data encryption and decryption.
- To convert readable text into encrypted ciphertext.
- To decrypt ciphertext using the correct secret key.
- To learn Python cryptography techniques.

## Technologies Used
- Python 3
- Cryptography Library
- Fernet Symmetric Encryption

## Features
- Encrypt user-entered text.
- Decrypt previously encrypted text.
- Generate an encryption key automatically.
- Handle invalid encrypted input.
- Simple command-line interface.

## Project Structure
```text
Data-Encryption-Decryption/
├── encryption.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements
- Python 3.x
- Cryptography library

## Installation
Install the required library:

```bash
pip install -r requirements.txt
```

## How to Run
1. Download or clone the repository.
2. Open a terminal in the project folder.
3. Install the required package.
4. Run the Python program:

```bash
python encryption.py
```

5. Choose option 1 to encrypt text or option 2 to decrypt text.

## Security Note
The encryption key is generated and stored locally in `key.key`. Keep this key private and never upload it to a public GitHub repository. Use the same key to decrypt previously encrypted text. If the key is lost, the encrypted text may not be recoverable.

This project is intended for educational purposes.

## Author
**Shivaani Shree SR**

## Conclusion
This project demonstrates the basic principles of symmetric encryption and decryption using Python and the Fernet cryptography library.
