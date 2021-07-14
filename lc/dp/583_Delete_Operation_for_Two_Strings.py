class Solution:
    def dp(self, word1, word2, i, j):
        if i == len(word1):
            return len(word2) - j
        elif j == len(word2):
            return len(word1) - i
        elif word1[i] == word2[j]:
            return self.dp(word1, word2, i + 1, j + 1)
        else:
            return 1 + min(self.dp(word1, word2, i + 1, j), self.dp(word1, word2, i, j + 1))

    def minDistance(self, word1: str, word2: str) -> int:
        return self.dp(word1, word2, 0, 0)

    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance('abcde', 'ace'))
    print(s.minDistance('sea', 'eat'))

    print(s.minDistance2('abcde', 'ace'))
    print(s.minDistance2('sea', 'eat'))
