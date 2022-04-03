# https://leetcode.com/problems/first-unique-character-in-a-string
# O(N) T | O(1) S


def first_unique_character_in_a_string(string: str) -> int:
    character_frequencies = {}

    for character in string:
        character_frequencies[character] = character_frequencies.get(character, 0) + 1

    for index, character in enumerate(string):
        if character_frequencies[character] == 1:
            return index

    return -1
