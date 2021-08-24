N, V = map(int, input().split())
weight = []
val = []
for i in range(N):
    v, w = map(int, input().split())
    val.append(v)
    weight.append(w)


# print(weight)
# print(val)

dp = [[0] * (V + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, V + 1):
        if j - weight[i - 1] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + val[i - 1])
print(dp[-1][-1])
