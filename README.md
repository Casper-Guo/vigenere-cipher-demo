# A basic demostration of the Vigenere cipher and the Kasiski examination

The encrypt and decrypt files implement both Caesar and Vigenere cipher. `utils.py` implements a few helper functions that showcases key aspects of the [Kasiski examination](https://en.wikipedia.org/wiki/Kasiski_examination).

Both encrypt files require the following command line arguments in order:

- input-file: a text file.
- output-file: a text file to store the encrypted text. If it doesn't exist, it will be created.
- key: the encryption key for the Vigenere cipher or the offset for the Caesar cipher.

Both decrypt files require the following command line arguments in order:

- input-file: a text file.
- output-file: a text file to store the decrypted text. If it doesn't exist, it will be created.
- key: the encryption key for the Vigenere cipher or the offset for the Ceasar cipher.

`utils.py` contains the following helper functions:

- `infer_key`: given a segment of encrypted and correspoinding plain text, infer the encryption key.
- `plot_frequency`: given the encrypted document and a candidate key length, plot the letter distribution that is encrypted by each key letter.
- `find_identical`: find all repeated sequences of a certain length and return their beginning indices.
