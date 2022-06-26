# https://leetcode.com/problems/max-consecutive-ones-iii
# O(N) T | O(1) S


def find_max_consecutive_ones(nums: list[int], k: int) -> int:
    consecutive_zero_count = 0
    start = 0
    max_length = 0
    for end, num in enumerate(nums):
        if num == 0:
            consecutive_zero_count += 1

        # If the number of 0 are more then k, it is the time to shrink the window
        while consecutive_zero_count > k:
            if nums[start] == 0:
                consecutive_zero_count -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length
