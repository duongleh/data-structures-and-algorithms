# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii


# O(N) T | O(1) S
def best_time_to_buy_and_sell_stock_ii(prices: list[int]) -> int:
    total_profit = 0
    for day in range(1, len(prices)):
        profit = prices[day] - prices[day - 1]
        if profit > 0:
            total_profit += profit
    return total_profit


# O(N) TS
def best_time_to_buy_and_sell_stock_ii_top_down(prices: list[int]) -> int:
    memo = [[None] * 2 for _ in range(len(prices))]

    def max_profit(day: int, is_holding: bool) -> int:
        if day == len(prices):
            return 0

        if memo[day][int(is_holding)] is not None:
            return memo[day][int(is_holding)]

        skipping = max_profit(day + 1, is_holding)
        if is_holding:
            trading = max_profit(day + 1, not is_holding) + prices[day]
        else:
            trading = max_profit(day + 1, not is_holding) - prices[day]
        memo[day][int(is_holding)] = max(skipping, trading)
        return memo[day][int(is_holding)]

    return max_profit(0, False)
