# https://leetcode.com/problems/coin-change
# O(amount * len(coins)) T | O(amount) S

from math import inf


def coin_change(coins: list[int], amount: int) -> int:
    memo = [0] + [inf] * amount

    for sub_amount in range(1, amount + 1):
        for coin in coins:
            if sub_amount - coin < 0:
                continue
            memo[sub_amount] = min(1 + memo[sub_amount - coin], memo[sub_amount])

    return memo[amount] if memo[amount] != inf else -1
