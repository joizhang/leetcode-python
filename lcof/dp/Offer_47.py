from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxValue([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
