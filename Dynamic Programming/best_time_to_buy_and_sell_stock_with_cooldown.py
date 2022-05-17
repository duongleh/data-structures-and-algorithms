# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# O(N) TS


def best_time_to_buy_and_sell_stock_with_cooldown(prices: list[int]) -> int:
    memo = [[None] * 2 for _ in range(len(prices))]

    def max_profit(day, is_holding):
        if day >= len(prices):
            return 0

        if memo[day][int(is_holding)] is not None:
            return memo[day][int(is_holding)]

        skipping = max_profit(day + 1, is_holding)
        if is_holding:
            trading = max_profit(day + 2, not is_holding) + prices[day]
        else:
            trading = max_profit(day + 1, not is_holding) - prices[day]
        memo[day][int(is_holding)] = max(skipping, trading)
        return memo[day][int(is_holding)]

    return max_profit(0, False)
