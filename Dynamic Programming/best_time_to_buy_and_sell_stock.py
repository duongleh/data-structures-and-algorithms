# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# O(N) T | O(1) S


def best_time_to_buy_and_sell_stock_sliding_window(prices: list[int]) -> int:
    max_profit = 0
    buy_day = 0
    for sell_day in range(1, len(prices)):
        profit = prices[sell_day] - prices[buy_day]
        if profit < 0:
            buy_day = sell_day
        else:
            max_profit = max(max_profit, profit)
    return max_profit


def best_time_to_buy_and_sell_stock_kadane_algorithm(prices: list[int]) -> int:
    max_profit = current_profit = 0
    for index in range(1, len(prices)):
        current_profit = max(0, current_profit + prices[index] - prices[index - 1])
        max_profit = max(max_profit, current_profit)
    return max_profit
