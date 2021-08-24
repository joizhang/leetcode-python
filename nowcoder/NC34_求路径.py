#
#
# @param m int整型
# @param n int整型
# @return int整型
#
class Solution:
    def uniquePaths(self , m , n ):
        # write code here
        if not m or not n:
            return 0
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
