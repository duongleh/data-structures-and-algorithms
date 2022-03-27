# https://leetcode.com/problems/contains-duplicate/
# O(N) TS


def contains_duplicate(nums: list[int]) -> bool:
    number_frequencies = {}

    for num in nums:
        number_frequencies[num] = number_frequencies.get(num, 0) + 1
        if number_frequencies[num] > 1:
            return True

    return False
