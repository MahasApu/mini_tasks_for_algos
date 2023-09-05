from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        day = 0
        prev_price = prices[day]
        while day < len(prices):
            if prev_price < prices[day]:
                profit += prices[day] - prev_price
            prev_price = prices[day]
            day += 1
        return profit

