# https://leetcode.com/problems/min-cost-climbing-stairs
# O(N) T - O(1) S


def min_cost_climbing_stairs(cost: list[int]) -> int:
    second_last_stair = 0
    last_stair = 0
    for index in range(2, len(cost) + 1):
        current_stair = min(cost[index - 1] + last_stair, cost[index - 2] + second_last_stair)
        second_last_stair, last_stair = last_stair, current_stair

    return last_stair
