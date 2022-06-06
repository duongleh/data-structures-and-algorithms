# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# O(N) T | O(1) S


def remove_duplicates_from_sorted_array(nums) -> int:
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return left
