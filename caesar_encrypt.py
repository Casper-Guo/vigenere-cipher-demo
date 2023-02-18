import sys
import string


def encrypt(char, offset):
    char_idx = string.ascii_uppercase.index(char)

    return string.ascii_uppercase[(char_idx + offset) % 26]


def main():
    """Usage: python3 main.py <input_file> <output_file> <encryption-key>"""

    assert len(sys.argv) == 4
    assert sys.argv[3].isdigit()

    offset = int(sys.argv[3])
    assert 0 < offset < 26

    with open(sys.argv[1], 'r') as input_file:
        plaintext = input_file.read()

    plaintext = [char.upper() for char in plaintext if char.isalpha()]
    ciphered = []

    for char in plaintext:
        ciphered.append(encrypt(char, offset))

    with open(sys.argv[2], 'w+') as output_file:
        output_file.write(''.join(ciphered))

    return 0


if __name__ == '__main__':
    main()
