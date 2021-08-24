n = int(input())
h = list(map(int, input().split()))
m = int(input())
w = list(map(int, input().split()))

ans = 0
h.sort()
w.sort()

# 优先满足胃口最小的
i, j = 0, 0
while i < n and j < m:
    if h[i] <= w[j]:
        i += 1
        j += 1
        ans += 1
    else:
        j += 1
print(ans)
