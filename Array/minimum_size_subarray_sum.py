# https://leetcode.com/problems/minimum-size-subarray-sum
# O(N) T | O(1) S

from math import inf


def minimum_size_subarray_sum(target: int, nums: list[int]) -> int:
    min_size = inf
    current_sum = 0
    start = 0
    for end, num in enumerate(nums):
        current_sum += num
        if current_sum < target:
            continue
        while current_sum - nums[start] >= target:
            current_sum -= nums[start]
            start += 1
        min_size = min(min_size, end - start + 1)
    return min_size if min_size != inf else 0
