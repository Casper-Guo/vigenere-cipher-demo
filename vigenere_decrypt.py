import sys
import string


def decrypt(idx, char, key):
    row = key[idx % len(key)]
    row_idx = string.ascii_uppercase.index(row)
    column_idx = string.ascii_uppercase.index(char)

    return string.ascii_uppercase[(column_idx - row_idx) % 26]


def main():
    """Usage: python3 main.py <input_file> <output_file> <encryption-key>"""

    assert len(sys.argv) == 4
    assert sys.argv[3].isalpha()

    key = sys.argv[3].upper()

    with open(sys.argv[1], 'r') as input_file:
        ciphered = input_file.read()

    decrypted = []

    for idx, char in enumerate(ciphered):
        if not char.isalpha():
            continue
        decrypted.append(decrypt(idx, char.upper(), key))

    with open(sys.argv[2], 'w+') as output_file:
        output_file.write(''.join(decrypted))

    return 0


if __name__ == '__main__':
    main()
