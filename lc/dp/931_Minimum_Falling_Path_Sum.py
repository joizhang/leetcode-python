from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * (n + 2) for _ in range(n + 1)]
        # 套壳处理 - --两边均为最大值
        for i in range(n + 1):
            dp[i][0] = 999
            dp[i][n + 1] = 999
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i - 1][j - 1]
        ans = 999
        for i in range(0, n + 2):
            ans = min(ans, dp[n][i])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minFallingPathSum([[-19, 57], [-40, -5]]))
    print(s.minFallingPathSum([[-48]]))
