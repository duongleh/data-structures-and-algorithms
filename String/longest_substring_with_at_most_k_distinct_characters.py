# https://www.lintcode.com/problem/386
# O(N) T | O(K) S


def longest_substring_with_at_most_k_distinct_characters(string: str, k: int) -> int:
    character_frequency = {}
    start = 0
    max_length = 0

    for end, character in enumerate(string):
        character_frequency[character] = character_frequency.get(character, 0) + 1

        # If number of distinct characters exceeds K, shrink the window
        while len(character_frequency) > k:
            character_frequency[string[start]] -= 1
            if character_frequency[string[start]] == 0:
                character_frequency.pop(string[start])
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length
