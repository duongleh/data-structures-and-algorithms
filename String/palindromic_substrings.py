# https://leetcode.com/problems/palindromic-substrings
# O(N^2) T | O(1) S


def palindromic_substrings(string: str) -> int:
    total_substrings = 0

    def count_palindromic_subtrings(start: int, end: int) -> int:
        subtrings_count = 0
        while start >= 0 and end < len(string) and string[start] == string[end]:
            start -= 1
            end += 1
            subtrings_count += 1
        return subtrings_count

    for index, _ in enumerate(string):
        total_substrings += count_palindromic_subtrings(index, index)
        total_substrings += count_palindromic_subtrings(index, index + 1)
    return total_substrings
