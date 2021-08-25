from typing import List


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
    """
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        n = len(prices)
        s0 = [0] * n
        s1 = [0] * n
        s2 = [0] * n
        s0[0] = 0
        s1[0] = -prices[0]
        s2[0] = -2147483648
        for i in range(1, n):
            # can buy, ie, we have no stock now, and the max profit should
            # be ''last no stock profit'' or ''last rest profit''
            s0[i] = max(s0[i - 1], s2[i - 1])
            # can sell, ie, we now have stock, and the profit should be
            # ''last stock profit'' or ''last no stock but buy this time''
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            # we should sell then take a rest
            s2[i] = s1[i - 1] + prices[i]
        return max(s0[-1], s2[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))
    print(s.maxProfit([1]))
