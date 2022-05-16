# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv
# O(N*k) TS


def best_time_to_buy_and_sell_stock_iv(prices: list[int], k: int) -> int:
    memo = [[[None] * (k + 1) for _ in range(2)] for __ in range(len(prices))]

    def max_profit(index: int, can_sell: bool, transaction_remaining: int):
        if transaction_remaining == 0:
            return 0

        if index == len(prices):
            return 0

        if memo[index][int(can_sell)][transaction_remaining] is not None:
            return memo[index][int(can_sell)][transaction_remaining]

        holding = max_profit(index + 1, can_sell, transaction_remaining)
        if can_sell:
            trading = max_profit(index + 1, not can_sell, transaction_remaining - 1) + prices[index]
        else:
            trading = max_profit(index + 1, not can_sell, transaction_remaining) - prices[index]
        memo[index][int(can_sell)][transaction_remaining] = max(holding, trading)
        return memo[index][int(can_sell)][transaction_remaining]

    return max_profit(0, False, k)
