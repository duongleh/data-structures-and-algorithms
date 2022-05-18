# https://leetcode.com/problems/move-zeroes
# O(N) T | O(1) S


def move_zeroes(nums: list[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            continue
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
    return nums
