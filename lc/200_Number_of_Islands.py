from typing import List


class Solution:
    def dfs(self, grid, m, n, i, j):
        if not 0 <= i < m or not 0 <= j < n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, m, n, i - 1, j)
        self.dfs(grid, m, n, i, j + 1)
        self.dfs(grid, m, n, i + 1, j)
        self.dfs(grid, m, n, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, m, n, i, j)
                    ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    island = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(s.numIslands(island))

    island = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(s.numIslands(island))
