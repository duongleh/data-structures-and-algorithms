# https://leetcode.com/problems/longest-palindromic-substring


# O(N^2) T | O(1) S
def longest_palindromic_substring_expand_around_center(string: str) -> str:
    start = 0
    end = 0

    def find_palindromic_substring(start: int, end: int) -> int:
        while start >= 0 and end < len(string) and string[start] == string[end]:
            start -= 1
            end += 1
        return end - start - 1

    for index, _ in enumerate(string):
        odd_substring = find_palindromic_substring(index - 1, index + 1)
        even_substring = find_palindromic_substring(index, index + 1)
        max_substring = max(odd_substring, even_substring)
        if max_substring > end + 1 - start:
            start = index - (max_substring - 1) // 2
            end = index + max_substring // 2

    return string[start : end + 1]


# O(N^2) TS
def longest_palindromic_substring_dynamic_programming(string: str) -> str:
    length = len(string)
    memo = [[None] * length for _ in range(length)]
    start = end = 0

    def longest_substring(left: int, right: int):
        if memo[left][right] is not None:
            return memo[left][right]

        if left >= right:
            memo[left][right] = True
        elif string[left] == string[right] and longest_substring(left + 1, right - 1):
            memo[left][right] = True
            nonlocal end, start
            if right - left > end - start:
                start, end = left, right
        else:
            memo[left][right] = False
            longest_substring(left + 1, right)
            longest_substring(left, right - 1)

        return memo[left][right]

    longest_substring(0, length - 1)
    return string[start : end + 1]
