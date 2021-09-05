n, L = map(int, input().split())
parent = list(map(int, input().split()))
dp = [0] * n
height = 0
for i in range(n):
    dp[i] = dp[parent[i]] + 1
    height = max(height, dp[i])
if L <= height:
    print(L + 1)
else:
    print(min(n, height + 1 + (L - height) // 2))
