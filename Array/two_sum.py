# https://leetcode.com/problems/two-sum/
# O(N) TS


def two_sum(nums: list[int], target: int) -> list[int]:
    table = {}

    for index, number in enumerate(nums):
        if number in table:
            return [index, table[number]]

        table[target - number] = index

    return []
