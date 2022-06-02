# https://leetcode.com/problems/longest-substring-without-repeating-characters
# O(N) T | O(1) S


def longest_substring_without_repeating_characters(string: str) -> int:
    character_index = {}
    start = 0
    max_length = 0
    for end, character in enumerate(string):
        # In the current window, we will not have any end_character after its previous index.
        # And if the start index is already ahead of the last index of end_character, we'll not update the start index.
        if character in character_index and start <= character_index[character]:
            start = character_index[character] + 1

        character_index[character] = end
        max_length = max(max_length, end - start + 1)
    return max_length
