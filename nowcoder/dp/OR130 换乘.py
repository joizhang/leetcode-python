terminal, N = map(int, input().split())
lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))
lines.sort()
# print(lines)
# 从0到各站点的最少时间
dp = [-1] * (terminal + 1)
dp[0] = 0
for start, end, cost in lines:
    # 不可达
    if dp[start] == -1 or end > terminal:
        continue

    if dp[end] == -1:
        dp[end] = dp[start] + cost
    else:
        dp[end] = min(dp[end], dp[start] + cost)
print(dp[-1])
