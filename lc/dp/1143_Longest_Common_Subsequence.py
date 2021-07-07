class Solution:

    def dp(self, text1, text2, i, j):
        if i == -1 or j == -1:
            return 0
        elif text1[i] == text2[j]:
            return self.dp(text1, text2, i - 1, j - 1) + 1
        else:
            return max(self.dp(text1, text2, i - 1, j), self.dp(text1, text2, i, j - 1))

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        return self.dp(text1, text2, len(text1) - 1, len(text2) - 1)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence('abcde', 'ace'))
    print(s.longestCommonSubsequence('abc', 'abc'))
    print(s.longestCommonSubsequence('abc', 'def'))
