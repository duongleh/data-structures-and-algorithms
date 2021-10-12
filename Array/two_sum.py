# https://leetcode.com/problems/two-sum/
# O(N) TS

def twoSum(nums: List[int], target: int) -> List[int]:
    table = {}

    for index, number in enumerate(nums):
        if number in table:
            return [index, table[number]]

        table[target - number] = index

    return []
