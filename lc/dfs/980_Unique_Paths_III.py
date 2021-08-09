from typing import List


class Solution:
    def __init__(self):
        self.res = 0

    def dfs(self, grid, m, n, x, y, empty):
        if not 0 <= x < m or not 0 <= y < n or grid[x][y] < 0:
            return
        if grid[x][y] == 2:
            if empty == 0:
                self.res += 1
            return
        grid[x][y] = -2
        self.dfs(grid, m, n, x - 1, y, empty - 1)
        self.dfs(grid, m, n, x, y + 1, empty - 1)
        self.dfs(grid, m, n, x + 1, y, empty - 1)
        self.dfs(grid, m, n, x, y - 1, empty - 1)
        grid[x][y] = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        m, n, empty = len(grid), len(grid[0]), 1
        x, y = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    empty += 1
        self.dfs(grid, m, n, x, y, empty)
        return self.res


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
    print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
    print(s.uniquePathsIII([[0, 1], [2, 0]]))
