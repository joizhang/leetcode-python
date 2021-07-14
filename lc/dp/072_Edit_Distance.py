class Solution:
    def dp(self, word1, word2, i, j):
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        if word1[i] == word2[j]:
            return self.dp(word1, word2, i - 1, j - 1)
        else:
            return min(
                self.dp(word1, word2, i, j - 1) + 1,  # 插入
                self.dp(word1, word2, i - 1, j) + 1,  # 插入
                self.dp(word1, word2, i - 1, j - 1) + 1,  # 替换
            )

    def minDistance(self, word1: str, word2: str) -> int:
        return self.dp(word1, word2, len(word1) - 1, len(word2) - 1)

    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1,
                    )
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("horse", "ros"))
    print(s.minDistance("intention", "execution"))

    print(s.minDistance2("horse", "ros"))
    print(s.minDistance2("intention", "execution"))
    print(s.minDistance2("", "a"))
