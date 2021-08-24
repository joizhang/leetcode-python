from typing import List


class Solution:
    def knapsack(self, N: int, W: int, weight: List[int], val: List[int]) -> int:
        """
        0-1背包问题
        :param N: 物品数为 N
        :param W: 重量为 W
        :param weight: 第 i 个物品的重量为 wt[i]
        :param val: 第 i 个物品的价值为 val[i]
        :return:
        """
        # 定义状态转移数组dp[i][j]，表示前i个物品，背包重量为j的情况下能装的最大价值。
        dp = [[0] * (W + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                if j - weight[i - 1] < 0:
                    # dp[i-1][j]表示当前物品不放入背包
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + val[i - 1])
        return dp[N][W]


if __name__ == '__main__':
    s = Solution()
    print(s.knapsack(3, 4, [2, 1, 3], [4, 2, 3]))
