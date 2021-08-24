T = int(input())
directions = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}
for _ in range(T):
    n = int(input())
    grid = []
    # 分别表示第n步向该方向走需要花费的体力值
    for _ in range(4):
        grid.append(list(map(int, input().split())))
    # print(grid)
    cost, ans = 0, ''
    for i in range(n):
        tmp = [grid[0][i], grid[1][i], grid[2][i], grid[3][i]]
        cost_min = min(tmp)
        min_index = tmp.index(cost_min)
        cost += cost_min
        ans += directions[min_index]
    print(cost)
    print(ans)
