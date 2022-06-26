# https://leetcode.com/problems/permutation-in-string
# O(N + M) T | O(1) S


def permutation_in_string(pattern: str, string: str) -> bool:
    character_frequency = {}
    for character in pattern:
        character_frequency[character] = character_frequency.get(character, 0) + 1

    start = 0
    for end, character in enumerate(string):
        # Add new character into window
        character_frequency[character] = character_frequency.get(character, 0) - 1
        if character_frequency[character] == 0:
            character_frequency.pop(character)

        if not character_frequency:
            return True

        if end - start + 1 <= len(pattern):
            continue

        # Remove out of range character from window,
        # keeping the length of window equals to the length of pattern
        character_frequency[string[start]] = character_frequency.get(string[start], 0) + 1
        if character_frequency[string[start]] == 0:
            character_frequency.pop(string[start])

        if not character_frequency:
            return True

        start += 1

    return False
