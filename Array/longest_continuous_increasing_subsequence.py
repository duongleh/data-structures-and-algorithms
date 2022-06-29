# https://leetcode.com/problems/longest-continuous-increasing-subsequence
# O(N) T | O(1) S


def longest_continuous_increasing_subsequence(nums: list[int]) -> int:
    current_length = max_length = 1
    for index, num in enumerate(nums):
        if index > 0 and num > nums[index - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    return max_length
