from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(grid, m, n, i, j)
                    ans = max(ans, area)
        return ans

    def dfs(self, grid, m, n, i, j):
        if not 0 <= i < m or not 0 <= j < n or grid[i][j] == 0:
            return 0
        ans = 1
        grid[i][j] = 0
        ans += self.dfs(grid, m, n, i - 1, j) + \
               self.dfs(grid, m, n, i, j + 1) + \
               self.dfs(grid, m, n, i + 1, j) + \
               self.dfs(grid, m, n, i, j - 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    island = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(s.maxAreaOfIsland(island))
