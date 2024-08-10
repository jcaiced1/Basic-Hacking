# README for Voldemort Encryption and Decryption Scripts

## Overview

This repository contains two Python scripts, `voldemort.py` and `decrypt.py`, which are designed to encrypt and decrypt files in the same directory. The encryption uses the symmetric encryption method provided by the `cryptography` library's `Fernet` class. The `voldemort.py` script encrypts all files in the directory, except for itself, the decryption script, and the encryption key. The `decrypt.py` script allows for the decryption of those files, provided the correct secret phrase is entered.

## Files

### `voldemort.py`

This script is responsible for encrypting all files in the directory where it is executed, excluding itself, the decryption script (`decrypt.py`), and the encryption key file (`thekey.key`).

#### How It Works:
1. **File Listing**: The script creates a list of all files in the current directory, excluding `voldemort.py`, `thekey.key`, and `decrypt.py`.
2. **Key Generation**: It generates a random encryption key using the `Fernet` class.
3. **Key Storage**: The generated key is saved to a file named `thekey.key`.
4. **File Encryption**: Each file in the list is opened in binary read mode, encrypted using the generated key, and then overwritten with the encrypted content in binary write mode.
5. **Output Message**: After encryption, a message is printed, warning the user that their files have been encrypted and demanding a ransom.

#### Usage:
- Run the script in the directory containing the files you wish to encrypt. Ensure that `cryptography` is installed in your Python environment.

```bash
python3 voldemort.py
```

### `decrypt.py`

This script is used to decrypt the files encrypted by `voldemort.py`.

#### How It Works:
1. **File Listing**: The script creates a list of all files in the current directory, excluding `voldemort.py`, `thekey.key`, and itself (`decrypt.py`).
2. **Key Retrieval**: It reads the encryption key from `thekey.key`.
3. **Secret Phrase**: The script prompts the user to enter a secret phrase. The correct phrase is hardcoded as `"coffee"`.
4. **File Decryption**: If the correct secret phrase is entered, the script decrypts each file using the retrieved key and overwrites the encrypted files with the decrypted content.
5. **Output Message**: Upon successful decryption, a congratulatory message is displayed. If the wrong phrase is entered, the script prompts the user for more ransom.

#### Usage:
- To decrypt your files, run the script and enter the correct secret phrase when prompted.

```bash
python3 decrypt.py
```

## Important Notes

- **Security Warning**: These scripts are for educational purposes only. Encryption keys are stored in plaintext, and the secret phrase is hardcoded in the decryption script. This makes the implementation insecure for real-world use.
- **Dependencies**: Ensure that the `cryptography` library is installed. You can install it via pip:

```bash
pip install cryptography
```

- **Disclaimer**: Use these scripts responsibly. Encrypting files without the owner's consent is illegal and unethical.