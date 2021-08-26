# -*- coding:utf-8 -*-

class MinCost:
    def findMinCost(self, A, n, B, m, c0, c1, c2):
        # write code here
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 删除和插入顺序似乎不能替换
        # 删除
        for i in range(1, n + 1):
            dp[0][i] = i * c1
        # 插入
        for i in range(1, m + 1):
            dp[i][0] = i * c0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if B[i - 1] == A[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + c0,
                        dp[i][j - 1] + c1,
                        dp[i - 1][j - 1] + c2,
                    )
        return dp[-1][-1]


if __name__ == '__main__':
    s = MinCost()
    print(s.findMinCost("abc", 3, "adc", 3, 5, 3, 100))
