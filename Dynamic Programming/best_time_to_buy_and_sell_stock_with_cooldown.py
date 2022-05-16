# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# O(N) TS


def best_time_to_buy_and_sell_stock_with_cooldown(prices: list[int]) -> int:
    memo = [[None] * 2 for _ in range(len(prices))]

    def max_profit(day, can_sell):
        if day >= len(prices):
            return 0

        if memo[day][int(can_sell)] is not None:
            return memo[day][int(can_sell)]

        holding = max_profit(day + 1, can_sell)
        if can_sell:
            trading = max_profit(day + 2, not can_sell) + prices[day]
        else:
            trading = max_profit(day + 1, not can_sell) - prices[day]
        memo[day][int(can_sell)] = max(holding, trading)
        return memo[day][int(can_sell)]

    return max_profit(0, False)
