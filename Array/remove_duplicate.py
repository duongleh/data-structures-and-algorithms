# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# O(N) T - O(1) S

def removeDuplicates(nums) -> int:
    length = len(nums)
    index = 0
    while index < length:
        if index + 1 == length:
            break

        if nums[index] == nums[index+1]:
            nums.pop(index)
            index -= 1
            length -= 1

        index += 1

    return length
