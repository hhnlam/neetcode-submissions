class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            profit = max(prices[i+1:], default=0) - price
            if profit > max_profit: max_profit = profit
        return max_profit