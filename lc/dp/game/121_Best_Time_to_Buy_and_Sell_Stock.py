from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('+inf'), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            # print(dp)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit2([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit2([7, 6, 4, 3, 1]))
