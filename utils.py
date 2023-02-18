import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import string


def infer_key(ciphered, plaintext):
    """Infer possible key given ciphertext and plaintext."""
    assert len(ciphered) == len(plaintext)
    assert ciphered.isalpha() and plaintext.isalpha()

    ciphered = ciphered.upper()
    plaintext = plaintext.upper()

    key = []

    for i in range(len(ciphered)):
        cipher_idx = string.ascii_uppercase.index(ciphered[i])
        plain_idx = string.ascii_uppercase.index(plaintext[i])
        key.append(string.ascii_uppercase[(cipher_idx - plain_idx) % 26])

    return ''.join(key)


def plot_frequency(ciphered, keylength):
    """Plot letter frequencies with an assumed key length."""
    letter_sets = [[] for i in range(keylength)]

    for idx, char in enumerate(ciphered):
        letter_sets[idx % keylength].append(char)

    letter_freqs = []
    for set in letter_sets:
        letter_freq = {}

        for letter in set:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

        letter_freqs.append(letter_freq)

    fig, axes = plt.subplots(nrows=keylength,
                             ncols=1,
                             sharey=True,
                             dpi=200
                             )

    for idx, letter_freq in enumerate(letter_freqs):
        letters = list(letter_freq.keys())
        freq = list(letter_freq.values())
        data = pd.DataFrame({'letter': letters, 'freq': freq})
        data = data.sort_values(by='letter', ascending=True)

        sns.barplot(data=data,
                    x="letter",
                    y="freq",
                    ax=axes[idx]
                    )
    plt.show()
    return 0


def find_identical(ciphered, word_length):
    """Find identical letter sequences of a certain length."""
    sequences = {}

    for i in range(0, len(ciphered) - word_length + 1):
        segment = ciphered[i:i + word_length]

        if segment in sequences:
            sequences[segment].append(i)
        else:
            sequences[segment] = [i]

    repeated = [item for item in sequences.items() if len(item[1]) > 2]
    return sorted(repeated, key=lambda x: len(x[1]), reverse=True)


def main():
    with open("ciphered.txt", "r") as ciphered_file:
        ciphered = ciphered_file.read()

    print(find_identical(ciphered, 3))
    return 0


if __name__ == '__main__':
    main()
