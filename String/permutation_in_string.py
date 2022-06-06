# https://leetcode.com/problems/permutation-in-string
# O(len(pattern) + len(string)) T | O(1) S


def permutation_in_string(pattern: str, string: str) -> bool:
    character_frequency = {}
    for character in pattern:
        character_frequency[character] = character_frequency.get(character, 0) + 1

    start = 0
    for character in string:
        character_frequency[character] = character_frequency.get(character, 0) - 1
        while character_frequency[character] < 0:
            character_frequency[string[start]] = character_frequency.get(string[start], 0) + 1
            start += 1

        if character_frequency[character] == 0:
            character_frequency.pop(character)

        if not character_frequency:
            return True

    return False
