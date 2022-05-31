# https://leetcode.com/problems/maximum-average-subarray-i
# O(N) T | O(1) S


def maximum_average_subarray_i(nums: list[int], k: int) -> float:
    max_sum = current_sum = sum(nums[:k])
    for end in range(k, len(nums)):
        start = end - k
        current_sum += nums[end] - nums[start]
        max_sum = max(max_sum, current_sum)
    return max_sum / k
