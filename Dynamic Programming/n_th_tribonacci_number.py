# https://leetcode.com/problems/n-th-tribonacci-number
# O(N) T - O(1) S


def n_th_tribonacci_number(n: int) -> int:
    third_last_number = 0
    second_last_number = 1
    last_number = 1
    for _ in range(3, n + 1):
        current_number = third_last_number + second_last_number + last_number
        third_last_number, second_last_number, last_number = second_last_number, last_number, current_number

    return last_number if n > 0 else 0
