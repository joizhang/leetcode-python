from typing import List


class Solution:
    """
    -2, -3,  3
    -5, -10, 1
    10, 30, -5
    ||
    V
    7, 5,  2, m
    6, 11, 5, m
    1, 1,  6, 1
    m, m,  1, m
    start from dp[m-1][n-1]
    """

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        INT_MAX = (1 << 31) - 1
        m, n = len(dungeon), len(dungeon[0])
        dp = [[INT_MAX] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = need if need > 0 else 1
        # print(dp)
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
