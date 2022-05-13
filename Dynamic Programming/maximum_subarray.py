# https://leetcode.com/problems/maximum-subarray
# O(N) T | O(1) S

from math import inf


def maximum_subarray(nums: list[int]) -> int:
    current_sum = max_sum = -inf
    for num in nums:
        current_sum = max(num, num + current_sum)
        max_sum = max(max_sum, current_sum)
    return max_sum
