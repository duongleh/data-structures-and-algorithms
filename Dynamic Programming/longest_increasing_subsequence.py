# https://leetcode.com/problems/longest-increasing-subsequence
# O(N^2) T | O(N) S


def length_of_longest_increasing_subsequence(nums: list[int]) -> int:
    subsequences_length = [1] * len(nums)

    for index in range(len(nums) - 1, -1, -1):
        for next_index in range(index + 1, len(nums)):
            if nums[index] < nums[next_index]:
                subsequences_length[index] = max(
                    subsequences_length[index],
                    subsequences_length[next_index] + 1,
                )

    return max(subsequences_length)
