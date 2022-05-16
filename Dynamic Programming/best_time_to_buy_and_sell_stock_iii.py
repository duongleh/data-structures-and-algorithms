# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
# O(N) TS

from best_time_to_buy_and_sell_stock_iv import best_time_to_buy_and_sell_stock_iv


def best_time_to_buy_and_sell_stock_iii(prices: list[int]) -> int:
    return best_time_to_buy_and_sell_stock_iv(prices, 2)
