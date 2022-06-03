# https://leetcode.com/problems/max-consecutive-ones
# O(N) T | O(1) S


def find_max_consecutive_ones(nums: list[int]) -> int:
    current_consecutive_ones = max_consecutive_ones = 0
    for num in nums:
        if num == 1:
            current_consecutive_ones += 1
            max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
        else:
            current_consecutive_ones = 0
    return max_consecutive_ones
