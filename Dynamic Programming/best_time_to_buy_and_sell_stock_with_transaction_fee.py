# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
# O(N) TS


def best_time_to_buy_and_sell_stock_with_transaction_fee(prices: list[int], fee: int) -> int:
    memo = [[None] * 2 for _ in range(len(prices))]

    def max_profit(day: int, can_sell: bool) -> int:
        if day == len(prices):
            return 0

        if memo[day][int(can_sell)] is not None:
            return memo[day][int(can_sell)]

        holding = max_profit(day + 1, can_sell)
        if can_sell:
            trading = max_profit(day + 1, not can_sell) + prices[day] - fee
        else:
            trading = max_profit(day + 1, not can_sell) - prices[day]
        memo[day][int(can_sell)] = max(holding, trading)
        return memo[day][int(can_sell)]

    return max_profit(0, False)
