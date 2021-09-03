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
        """
        this problems can be reduced to finding the LCS
        between the original string and its reversed form
        """

        # s2 = s[::-1]
        # n = len(s)
        # dp = [[0] * (n + 1) for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     for j in range(1, n + 1):
        #         if s[i - 1] == s2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # return dp[-1][-1]

        n = len(s)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(1, n + 1):
            for j in reversed(range(1, n + 1)):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j + 1])
        return dp[n][1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindromeSubseq("bbbab"))
    print(s.longestPalindromeSubseq("cbbd"))

    print(s.longestPalindromeSubseq2("bbbab"))
    print(s.longestPalindromeSubseq2("cbbd"))
    print(s.longestPalindromeSubseq2("abc1234321ab"))
