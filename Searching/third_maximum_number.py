# https://leetcode.com/problems/third-maximum-number
# O(N) T - O(1) S

def third_max_number(array: list[int]) -> int:
    max_number = second_max_number = third_max_number = None
    for number in array:
        if number in [max_number, second_max_number, third_max_number]:
            continue
        if not max_number or number > max_number:
            number, max_number = max_number, number
        if not second_max_number or number > second_max_number:
            number, second_max_number = second_max_number, number
        if not third_max_number or number > third_max_number:
            third_max_number = number
    return max_number if third_max_number is None else third_max_number
