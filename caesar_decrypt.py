import sys
import string


def decrypt(char, offset):
    char_idx = string.ascii_uppercase.index(char)

    return string.ascii_uppercase[(char_idx - offset) % 26]


def main():
    """Usage: python3 main.py <input_file> <output_file> <encryption-key>"""

    assert len(sys.argv) == 4
    assert sys.argv[3].isdigit()

    offset = int(sys.argv[3])
    assert 0 < offset < 26

    with open(sys.argv[1], 'r') as input_file:
        ciphered = input_file.read()

    ciphered = [char.upper() for char in ciphered if char.isalpha()]
    plaintext = []

    for char in ciphered:
        plaintext.append(decrypt(char, offset))

    with open(sys.argv[2], 'w+') as output_file:
        output_file.write(''.join(plaintext))

    return 0


if __name__ == '__main__':
    main()
