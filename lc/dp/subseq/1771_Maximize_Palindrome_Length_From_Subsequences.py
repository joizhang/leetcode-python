class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in reversed(range(n - 1)):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if i < len(word1) <= j:
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('cacb', 'cbba'))
    print(s.longestPalindrome('ab', 'ab'))
    print(s.longestPalindrome('aa', 'bb'))
