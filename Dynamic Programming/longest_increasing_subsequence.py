# https://leetcode.com/problems/longest-increasing-subsequence


# O(N^2) T | O(N) S
def length_of_longest_increasing_subsequence_bottom_up(nums: list[int]) -> int:
    length = len(nums)
    subsequences_length = [1] * length

    for index in range(length):
        for previous_index in range(index):
            if nums[index] > nums[previous_index]:
                subsequences_length[index] = max(
                    subsequences_length[index],
                    subsequences_length[previous_index] + 1,
                )

    return max(subsequences_length)


# O(N^2) TS
def length_of_longest_increasing_subsequence_top_down(nums: list[int]) -> int:
    length = len(nums)
    memo = [[None] * (length + 1) for _ in range(length)]

    def longest_subsequence(index: int, previous_index: int) -> int:
        if index == len(nums):
            return 0

        if memo[index][previous_index] is not None:
            return memo[index][previous_index]

        memo[index][previous_index] = longest_subsequence(index + 1, previous_index)
        if previous_index == -1 or nums[index] > nums[previous_index]:
            memo[index][previous_index] = max(
                longest_subsequence(index + 1, index) + 1,
                memo[index][previous_index],
            )

        return memo[index][previous_index]

    return longest_subsequence(0, -1)
