from typing import List


class Solution:
    def dp(self, coins, n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('+inf')
        for coin in coins:
            sub_problem = self.dp(coins, n - coin)
            if sub_problem < 0:
                continue
            res = min(res, 1 + sub_problem)
        return res if res != float('+inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        # 暴力解法
        return self.dp(coins, amount)

    def coinChange2(self, coins: List[int], amount: int) -> int:
        # 动态规划
        # dp 数组的定义：当目标金额为 x 时，至少需要 dp[x] 枚硬币凑出。
        dp = [amount + 1] * (amount + 1)
        # base case
        dp[0] = 0
        for x in range(1, amount + 1):
            for coin in coins:
                # 子问题无解，跳过
                if x - coin < 0:
                    continue
                dp[x] = min(dp[x], 1 + dp[x - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([2], 3))
    print(s.coinChange([1], 0))
    print(s.coinChange([1], 1))
    print(s.coinChange([1], 2))

    print(s.coinChange2([1, 2, 5], 11))
    print(s.coinChange2([2], 3))
    print(s.coinChange2([1], 0))
    print(s.coinChange2([1], 1))
    print(s.coinChange2([1], 2))
