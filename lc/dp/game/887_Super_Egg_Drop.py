class Solution:
    """
    https://leetcode-cn.com/problems/super-egg-drop/solution/ji-dan-diao-luo-xiang-jie-by-shellbye/
    """
    def dp(self, k, n):
        if n == 0 or n == 1 or k == 1:
            return n
        res = n
        # 穷举所有可能的选择
        for i in range(1, n + 1):
            t_min = max(
                self.dp(k, n - i),  # 没碎
                self.dp(k - 1, i - 1)  # 碎了
            )
            res = min(res, 1 + t_min)
        return res

    def superEggDrop(self, k: int, n: int) -> int:
        return self.dp(k, n)

    def superEggDrop2(self, k: int, n: int) -> int:
        # time: O(KN^2)
        # space: O(KN)
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, n + 1):
            dp[0][i] = 0  # no egg
            dp[1][i] = i  # one egg
        for i in range(1, k + 1):
            dp[i][0] = 0  # zero floor

        for i in range(2, k + 1):
            for j in range(1, n + 1):
                t_min_drop = n * n
                for x in range(1, j + 1):
                    t_min_drop = min(t_min_drop, 1 + max(dp[i - 1][x - 1], dp[i][j - x]))
                dp[i][j] = t_min_drop
        return dp[k][n]

    def superEggDrop3(self, k: int, n: int) -> int:
        # time O(KN)
        dp = [0] * (n + 1)
        # only one egg situation
        for i in range(n + 1):
            dp[i] = i
        # two and more eggs
        for i in range(2, k + 1):
            dp2 = [0] * (n + 1)
            x = 1
            for j in range(1, n + 1):
                while x < j and max(dp[x - 1], dp2[j - x]) > max(dp[x], dp2[j - x - 1]):
                    x += 1
                dp2[j] = 1 + max(dp[x - 1], dp2[j - x])
            dp = dp2
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.superEggDrop(2, 10))
    print(s.superEggDrop2(2, 100))
    print(s.superEggDrop3(4, 5000))
