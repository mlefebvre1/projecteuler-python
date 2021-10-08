from pathlib import Path
from functools import reduce
from typing import List, Iterable

from ..utils.timeit import timeit


def seperate_cipher_into_3_streams(cipher: List[str]) -> List[List[str]]:
    streams = [[], [], []]
    for i, value in enumerate(cipher):
        streams[i % 3].append(value)
    return streams


def count_repetitions(stream: List[str]) -> List[int]:
    repetitions = [0] * 256
    for x in stream:
        repetitions[int(x)] += 1
    return repetitions


def decode_text(cipher: List[str], keys: List[int]) -> Iterable[str]:
    for index, character in enumerate(cipher):
        if index % 3 == 0:
            yield chr(int(character) ^ keys[0])
        elif index % 3 == 1:
            yield chr(int(character) ^ keys[1])
        elif index % 3 == 2:
            yield chr(int(character) ^ keys[2])


@timeit
def problem59():
    """

    XOR decryption
    Problem 59

    Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code
     for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

    A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given
    value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the
    cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

    For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
    bytes. The user would keep the encrypted message and the encryption key in different locations, and without both
    "halves", it is impossible to decrypt the message.

    Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If
    the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
    The balance for this method is using a sufficiently long password key for security, but short enough to be
    memorable.

    Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt
    (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the
    plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the
    original text
    """
    with open(f"{Path(__file__).parent}/data/problem59.txt", "r") as fp:
        fp_data = fp.read()
        fp.close()

    cipher = fp_data.split(",")
    streams = seperate_cipher_into_3_streams(cipher)
    keys = []
    for i, stream in enumerate(streams):
        repetitions = list(zip(range(0, 256), count_repetitions(stream)))
        # if we assume that the most common character in a text is a space, then for each stream, we assume that most
        # repeated value is an encoded space. If we xor with a space character, then we should find the key we are
        # looking for
        encoded_space = max(repetitions, key=lambda x: x[1])
        keys.append(encoded_space[0] ^ ord(" "))
    decoded_text = "".join(list(decode_text(cipher, keys)))
    return reduce(lambda total, char: total + ord(char), decoded_text, 0)


if __name__ == "__main__":
    problem59()
