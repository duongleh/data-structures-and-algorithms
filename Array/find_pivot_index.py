# https://leetcode.com/problems/find-pivot-index
# O(N) T | O(1) S


def find_pivot_index(nums: list[int]) -> int:
    left = 0
    right = sum(nums)
    for index, num in enumerate(nums):
        right -= num
        if left == right:
            return index
        left += num
    return -1
