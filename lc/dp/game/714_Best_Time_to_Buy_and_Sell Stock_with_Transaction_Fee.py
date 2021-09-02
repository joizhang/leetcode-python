from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        days = len(prices)
        buy = [0] * days
        sell = [0] * days
        buy[0] = -prices[0] - fee
        for i in range(1, days):
            # keep the same as day i-1, or buy from sell status at day i-1
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i] - fee)
            # keep the same as day i-1, or sell from buy status at day i-1
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        return sell[-1]
