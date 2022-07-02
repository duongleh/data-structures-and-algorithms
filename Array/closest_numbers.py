# https://www.hackerrank.com/challenges/closest-numbers
# O(Nlog(N)) T | O(N) S

from math import inf


def closest_numbers(nums):
    nums.sort()
    pairs = []
    min_difference = inf
    for index in range(1, len(nums)):
        difference = nums[index] - nums[index - 1]
        if difference < min_difference:
            pairs = [(nums[index - 1], nums[index])]
            min_difference = difference
        elif difference == min_difference:
            pairs.append((nums[index - 1], nums[index]))
    return pairs
