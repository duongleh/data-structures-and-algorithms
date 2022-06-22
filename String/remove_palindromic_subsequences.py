# https://leetcode.com/problems/remove-palindromic-subsequences
# O(N) T | O(1) S

from valid_palindrome import is_palindrome


def remove_palindromic_subsequences(string: str) -> int:
    if not string:
        return 0
    if is_palindrome(string):
        return 1
    return 2
