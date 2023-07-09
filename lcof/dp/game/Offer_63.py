from typing import List


class Solution:
    """剑指 Offer 63. 股票的最大利润"""

    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('+inf'), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
