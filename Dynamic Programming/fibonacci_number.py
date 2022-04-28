# https://leetcode.com/problems/fibonacci-number


# O(N) TS
def fibonacci_number_top_down(n: int, memoize: dict = None) -> int:
    if memoize is None:
        memoize = {0: 0, 1: 1}
    if n not in memoize:
        memoize[n] = fibonacci_number_top_down(n - 1, memoize) + fibonacci_number_top_down(n - 2, memoize)
    return memoize[n]


# O(N) T - O(1) S
def fibonacci_number_bottom_up(n: int) -> int:
    second_last_number = 0
    last_number = 1
    for _ in range(n - 1):
        second_last_number, last_number = last_number, last_number + second_last_number
    return last_number if n > 0 else second_last_number
