# https://leetcode.com/problems/minimum-window-substring
# O(len(string + len(pattern))) T | O(1) S

from math import inf


def minimum_window_substring(string: str, pattern: str) -> str:
    character_frequency = {}
    for character in pattern:
        character_frequency[character] = character_frequency.get(character, 0) + 1

    min_substring_length, min_substring_start, min_substring_end = inf, 0, -1
    matched_characters = 0
    start = 0
    for end, character in enumerate(string):
        if character not in character_frequency:
            continue

        character_frequency[character] = character_frequency.get(character, 0) - 1
        if character_frequency[character] >= 0:
            matched_characters += 1

        if matched_characters == len(pattern):
            # Try to shrink the window from the beginning
            while character_frequency.get(string[start], -1) < 0:
                if string[start] in character_frequency:
                    character_frequency[string[start]] += 1
                start += 1

            # Keeping track of the smallest substring that has all the matching characters
            current_substring_length = end - start + 1
            if current_substring_length < min_substring_length:
                min_substring_length = current_substring_length
                min_substring_start, min_substring_end = start, end

    return string[min_substring_start : min_substring_end + 1]
