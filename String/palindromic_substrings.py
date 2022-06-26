# https://leetcode.com/problems/palindromic-substrings


# O(N^2) T | O(1) S
def palindromic_substrings_expand_around_center(string: str) -> int:
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


# O(N^2) TS
def palindromic_substrings_dynamic_programming(string: str) -> str:
    length = len(string)
    memo = [[None] * length for _ in range(length)]
    total_substrings = 0

    def count_substring(left: int, right: int):
        if memo[left][right] is not None:
            return memo[left][right]

        nonlocal total_substrings

        if left > right:
            memo[left][right] = True
        elif left == right:
            memo[left][right] = True
            total_substrings += 1
        elif string[left] == string[right] and count_substring(left + 1, right - 1):
            memo[left][right] = True
            total_substrings += 1
        else:
            memo[left][right] = False

        if left < right:
            count_substring(left + 1, right)
            count_substring(left, right - 1)

        return memo[left][right]

    count_substring(0, length - 1)
    return total_substrings
