# https://leetcode.com/problems/valid-anagram
# O(N + M) T | O(1) S


def is_anagram(first_string: str, second_string: str) -> bool:
    if len(first_string) != len(second_string):
        return False

    character_frequency = {}
    for character in first_string:
        character_frequency[character] = character_frequency.get(character, 0) + 1

    for character in second_string:
        if character not in character_frequency:
            return False

        character_frequency[character] -= 1
        if character_frequency[character] == 0:
            character_frequency.pop(character)

    return not character_frequency
