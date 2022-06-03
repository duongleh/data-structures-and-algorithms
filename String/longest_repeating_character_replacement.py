# https://leetcode.com/problems/longest-repeating-character-replacement
# O(N) T | O(1) S


def longest_repeating_character_replacement(string: str, k: int) -> int:
    character_frequency = {}
    start = 0
    max_length = 0
    for end, character in enumerate(string):
        character_frequency[character] = character_frequency.get(character, 0) + 1

        # If the total of minority letters is more than K,
        # we should shrink the window.
        while end - start + 1 - max(character_frequency.values()) > k:
            character_frequency[string[start]] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length
