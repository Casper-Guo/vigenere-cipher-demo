import os
import sys
import string


def encrypt(idx, char, key):
    row = key[idx % len(key)]
    row_idx = string.ascii_uppercase.index(row)
    column_idx = string.ascii_uppercase.index(char)

    return string.ascii_uppercase[(row_idx + column_idx) % 26]


def main():
    """Usage: python3 main.py <input_file> <output_file> <encryption-key>"""

    assert len(sys.argv) == 4
    assert sys.argv[3].isalpha()

    key = sys.argv[3].upper()

    with open(sys.argv[1], 'r') as input_file:
        plaintext = input_file.read()

    plaintext = [char.upper() for char in plaintext if char.isalpha()]
    ciphered = []

    for idx, char in enumerate(plaintext):
        if not char.isalpha():
            continue
        ciphered.append(encrypt(idx, char, key))

    with open(sys.argv[2], 'w+') as output_file:
        output_file.write(''.join(ciphered))

    return 0


if __name__ == '__main__':
    main()
