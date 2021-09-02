from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 所有上涨交易日都买卖
        n = len(prices)
        dp = [0] * n
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                dp[i] = prices[i] - prices[i - 1] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]
            # print(dp)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
