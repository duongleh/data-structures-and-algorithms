# https://leetcode.com/problems/longest-common-subsequence
# O(N*M) TS (N, M is the length of text1, text2 respectively)


def longest_common_subsequence_top_down(
    text1: str,
    text2: str,
    index1: int = 0,
    index2: int = 0,
    memo: list[list] = None,
) -> int:
    if memo is None:
        memo = [[None] * len(text1) for _ in range(len(text2))]

    if index1 >= len(text1) or index2 >= len(text2):
        return 0

    if memo[index2][index1] is None:
        if text1[index1] == text2[index2]:
            memo[index2][index1] = 1 + longest_common_subsequence_top_down(text1, text2, index1 + 1, index2 + 1, memo)
        else:
            memo[index2][index1] = max(
                longest_common_subsequence_top_down(text1, text2, index1, index2 + 1, memo),
                longest_common_subsequence_top_down(text1, text2, index1 + 1, index2, memo),
            )

    return memo[index2][index1]


def longest_common_subsequence_bottom_up(text1: str, text2: str) -> int:
    memo = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

    for index1 in range(len(text1) - 1, -1, -1):
        for index2 in range(len(text2) - 1, -1, -1):
            if text1[index1] == text2[index2]:
                memo[index2][index1] = 1 + memo[index2 + 1][index1 + 1]
            else:
                memo[index2][index1] = max(
                    memo[index2][index1 + 1],
                    memo[index2 + 1][index1],
                )

    return memo[0][0]
