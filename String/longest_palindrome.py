# https://leetcode.com/problems/longest-palindrome
# O(N) T | O(1) S (the alphabet size is fixed)


def longest_palindrome(string: str) -> int:
    character_frequency = {}
    for character in string:
        character_frequency[character] = character_frequency.get(character, 0) + 1

    max_length = 0
    for character, frequency in character_frequency.items():
        max_length += frequency
        if frequency % 2 != 0:
            max_length -= 1

    return max_length if max_length == len(string) else max_length + 1
