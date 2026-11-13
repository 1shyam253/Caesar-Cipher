# Caesar Cipher 🔑

A beginner-friendly Python cryptography project that encrypts and
decrypts text by shifting each letter by a fixed amount — a classic
first step into cryptography and cybersecurity.

## Features

- Encrypts text with any shift amount (default: 3)
- Decrypts text with the same shift
- Brute-force mode tries all 25 shifts, showing why Caesar is weak
- Keeps uppercase, lowercase, and non-letters (spaces, punctuation) as they are
- Uses only the Python standard library — no third-party packages

## Requirements

- Python 3.8 or newer
- No third-party packages are required

## How to run

Encrypt text (shift 3 by default):

```bash
python caesar_cipher.py "Hello World"
```

On some systems, use `python3 caesar_cipher.py "Hello World"`.

### Examples

Encrypt with a shift of 5:

```bash
python caesar_cipher.py "Hello World" --shift 5
```

Decrypt text:

```bash
python caesar_cipher.py "Mjqqt Btwqi" --shift 5 --decrypt
```

Try all 25 shifts on an encrypted message:

```bash
python caesar_cipher.py "Khoor Zruog" --brute-force
```

## How it works

Each letter is shifted forward in the alphabet by the shift amount.
With a shift of 3, A becomes D, B becomes E, and Z wraps around to C.
Decrypting shifts the letters back by the same amount.

## Project structure

```text
caesar-cipher/
├── caesar_cipher.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Learning outcomes

- Basic cryptography and the Caesar cipher
- String and character handling in Python
- Command-line arguments with `argparse`
- Why simple ciphers are easy to break (brute force)

## Author

SHANMUKHA SREE LALITHA VENKAT SHYAM PYNA ([@1shyam253](https://github.com/1shyam253))
