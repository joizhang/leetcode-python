from typing import List


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/149383/Easy-DP-solution-using-state-machine-O(n)-time-complexity-O(1)-space-complexity
    """
    def maxProfit(self, prices: List[int]) -> int:
        # We begin at state 0, where we can either rest (i.e. do nothing) or buy stock at a given price.
        s1 = -prices[0]
        # From state 1, we can once again choose to do nothing or we can sell our stock.
        s2 = -(1 << 31)
        # From state 2, we can choose to do nothing or buy more stock.
        s3 = -(1 << 31)
        # From state 3, we can once again choose to do nothing or we can sell our stock for the last time.
        s4 = -(1 << 31)
        for i in range(1, len(prices)):
            s1 = max(s1, -prices[i])
            s2 = max(s2, s1 + prices[i])
            s3 = max(s3, s2 - prices[i])
            s4 = max(s4, s3 + prices[i])
        return max(0, s4)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
    print(s.maxProfit([1]))
