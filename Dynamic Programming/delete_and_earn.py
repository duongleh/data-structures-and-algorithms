# https://leetcode.com/problems/delete-and-earn
# When k is large compared to N, approach 2 is faster.
# When N is not large compared to k, we should use approach 1.


# O(N + k) T | O(N) S (k is the maximum element in nums)
def delete_and_earn_1(nums: list[int]) -> int:
    points = {}
    max_num = 0
    for num in nums:
        points[num] = num + points.get(num, 0)
        max_num = max(max_num, num)

    second_last_earning = 0
    last_earning = 0

    for num in range(max_num + 1):
        current_earning = max(points.get(num, 0) + second_last_earning, last_earning)
        second_last_earning, last_earning = last_earning, current_earning

    return last_earning


# O(Nlog(N)) T | O(N) S
def delete_and_earn_2(nums: list[int]) -> int:
    points = {}
    for num in nums:
        points[num] = num + points.get(num, 0)

    sorted_nums = sorted(points.keys())

    second_last_earning = 0
    last_earning = 0

    for index, num in enumerate(sorted_nums):
        if index and sorted_nums[index - 1] + 1 == num:
            current_earning = max(points[num] + second_last_earning, last_earning)
        else:
            current_earning = points[num] + last_earning
        second_last_earning, last_earning = last_earning, current_earning

    return last_earning
