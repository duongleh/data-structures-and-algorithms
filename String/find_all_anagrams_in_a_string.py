# https://leetcode.com/problems/find-all-anagrams-in-a-string
# O(N + M) T | O(1) S


def find_all_anagrams_in_a_string(string: str, pattern: str) -> list[int]:
    character_frequency = {}
    for character in pattern:
        character_frequency[character] = character_frequency.get(character, 0) + 1

    start = 0
    anagram_indexes = []
    for end, character in enumerate(string):
        character_frequency[character] = character_frequency.get(character, 0) - 1

        if character_frequency[character] == 0:
            character_frequency.pop(character)

        if end - start + 1 > len(pattern):
            character_frequency[string[start]] = character_frequency.get(string[start], 0) + 1
            if character_frequency[string[start]] == 0:
                character_frequency.pop(string[start])
            start += 1

        if not character_frequency:
            anagram_indexes.append(start)

    return anagram_indexes
