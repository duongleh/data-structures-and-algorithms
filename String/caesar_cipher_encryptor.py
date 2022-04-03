# https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
# O(N) TS


def caesar_cipher_encryptor(string, key):
    new_string = []

    for character in string:
        ascii_letter = ord(character)
        new_ascii_letter = ascii_letter + key % 26

        if (65 <= ascii_letter <= 90 and new_ascii_letter > 90) or (
            97 <= ascii_letter <= 122 and new_ascii_letter > 122
        ):
            new_ascii_letter -= 26

        new_string.append(chr(new_ascii_letter))

    return "".join(new_string)
