# https://leetcode.com/problems/longest-palindromic-subsequence
# O(N^2) TS


def longest_palindromic_subsequence(string: str) -> int:
    length = len(string)
    memo = [[None] * length for _ in range(length)]

    def longest_subsequence(left: int, right: int):
        if memo[left][right] is not None:
            return memo[left][right]

        if left > right:
            return 0

        if left == right:
            return 1

        if string[left] == string[right]:
            memo[left][right] = 2 + longest_subsequence(left + 1, right - 1)
        else:
            memo[left][right] = max(
                longest_subsequence(left, right - 1),
                longest_subsequence(left + 1, right),
            )

        return memo[left][right]

    return longest_subsequence(0, length - 1)
