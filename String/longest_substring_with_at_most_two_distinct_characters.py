# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters
# https://leetcode.com/problems/fruit-into-baskets
# O(N) T | O(1) S


from longest_substring_with_at_most_k_distinct_characters import longest_substring_with_at_most_k_distinct_characters


def longest_substring_with_at_most_two_distinct_characters(string: str) -> int:
    return longest_substring_with_at_most_k_distinct_characters(string, 2)
