# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
# O(N) T | O(1) S


def remove_duplicates_from_sorted_array_ii(nums: list[int]) -> int:
    left = 1
    count = 1
    for right in range(1, len(nums)):
        if nums[right] == nums[right - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[left] = nums[right]
            left += 1
    return left
