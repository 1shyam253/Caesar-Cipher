"""Caesar Cipher — a beginner-friendly Python cryptography project.

Encrypts and decrypts text by shifting each letter by a fixed amount.
A classic first step into cryptography and cybersecurity.
"""

import argparse
import string
import sys

ALPHABET_SIZE = 26


def caesar(text: str, shift: int, encrypt: bool = True) -> str:
    """Shift each letter in text by shift positions."""
    if not encrypt:
        shift = -shift
    result = []
    for char in text:
        if char in string.ascii_lowercase:
            base = ord("a")
            result.append(chr((ord(char) - base + shift) % ALPHABET_SIZE + base))
        elif char in string.ascii_uppercase:
            base = ord("A")
            result.append(chr((ord(char) - base + shift) % ALPHABET_SIZE + base))
        else:
            result.append(char)
    return "".join(result)


def brute_force(text: str):
    """Try every shift (1-25) and return a list of (shift, plaintext)."""
    return [(shift, caesar(text, shift, encrypt=False)) for shift in range(1, ALPHABET_SIZE)]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Encrypt or decrypt text with a Caesar cipher.")
    parser.add_argument("text", nargs="?", help="Text to encrypt or decrypt")
    parser.add_argument("--shift", type=int, default=3, help="Shift amount (default: 3)")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt instead of encrypting")
    parser.add_argument("--brute-force", action="store_true",
                        help="Try all 25 shifts and show every result")
    args = parser.parse_args(argv)

    if not args.text:
        parser.print_usage(sys.stderr)
        print("Error: provide some text to encrypt or decrypt.", file=sys.stderr)
        return 2

    print("=" * 40)
    print("          CAESAR CIPHER")
    print("=" * 40)
    print(f"Input:  {args.text}")
    if args.brute_force:
        print("\nTrying all shifts:")
        for shift, result in brute_force(args.text):
            print(f"  shift {shift:>2}: {result}")
    else:
        action = "Decrypted" if args.decrypt else "Encrypted"
        print(f"Shift:  {args.shift}")
        print(f"{action}: {caesar(args.text, args.shift, encrypt=not args.decrypt)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
