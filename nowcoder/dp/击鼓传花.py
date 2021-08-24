n, m = tuple(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(m + 1)]
dp[0][1] = 1
dp[1][n] = 1
dp[1][2] = 1
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if j == 1:
            dp[i][j] = dp[i - 1][n] + dp[i - 1][2]
        elif j == n:
            dp[i][j] = dp[i - 1][1] + dp[i - 1][n - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(dp[m][1])
