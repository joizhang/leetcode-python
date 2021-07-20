from typing import List


class Solution:
    def knapsack(self, N: int, W: int, wt: List[int], val: List[int]) -> int:
        # 对于前 i 个物品，当前背包的容量为 j，这种情况下可以装的最大价值是 dp[i][j]
        dp = [[0] * (W + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                if i - wt[i - 1] < 0:
                    # 这种情况下只能选择不装入背包
                    dp[i][j] = dp[i - 1][w]
                else:
                    dp[i][w] =


if __name__ == '__main__':
    s = Solution()
    print(s.knapsack(3, 4, [2, 1, 3], [4, 2, 3]))
