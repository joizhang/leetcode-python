class Solution:
    def dp(self, s, left, right):
        if left > right:
            return 0
        elif left == right:
            return 1
        else:
            if s[left] == s[right]:
                return 2 + self.dp(s, left + 1, right - 1)
            else:
                return max(self.dp(s, left + 1, right), self.dp(s, left, right - 1))

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.dp(s, 0, len(s) - 1)

    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindromeSubseq("bbbab"))
    print(s.longestPalindromeSubseq("cbbd"))

    print(s.longestPalindromeSubseq2("bbbab"))
    print(s.longestPalindromeSubseq2("cbbd"))
