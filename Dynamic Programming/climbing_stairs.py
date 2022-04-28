# https://leetcode.com/problems/climbing-stairs
# O(N) T - O(1) S


def climbing_stairs(n: int) -> int:
    second_last_stair, last_stair = 1, 2
    for _ in range(n - 2):
        second_last_stair, last_stair = last_stair, last_stair + second_last_stair
    return last_stair if n > 1 else second_last_stair
