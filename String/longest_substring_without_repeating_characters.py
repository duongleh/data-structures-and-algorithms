# https://leetcode.com/problems/longest-substring-without-repeating-characters
# O(N) T | O(1) S


def longest_substring_without_repeating_characters(string: str) -> int:
    character_frequency = set()
    max_length = 0
    start = 0

    for end, character in enumerate(string):
        while character in character_frequency:
            character_frequency.remove(string[start])
            start += 1

        character_frequency.add(character)
        max_length = max(max_length, end - start + 1)

    return max_length
