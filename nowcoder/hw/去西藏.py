"""
3 4
1 0 0 0
0 0 0 0
0 0 2 -1
"""

m, n = list(map(int, input().split()))
matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split())))


def dfs(x_, y_, empty_):
    if not 0 <= x_ < m or not 0 <= y_ < n or matrix[x_][y_] < 0:
        return 0
    if matrix[x_][y_] == 2:
        return 1 if empty_ == 0 else 0

    ans_ = 0
    matrix[x_][y_] = -2
    ans_ += dfs(x_ - 1, y_, empty_ - 1)
    ans_ += dfs(x_, y_ + 1, empty_ - 1)
    ans_ += dfs(x_ + 1, y_, empty_ - 1)
    ans_ += dfs(x_, y_ - 1, empty_ - 1)
    matrix[x_][y_] = 0
    return ans_


x, y, empty = 0, 0, 1
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            empty += 1

ans = dfs(x, y, empty)
print(ans)
