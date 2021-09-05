from typing import List


class Solution:
    def dfs(self, matrix, m, n, i, j, cache):
        if cache[i][j]:
            return cache[i][j]

        val = matrix[i][j]
        a1 = self.dfs(matrix, m, n, i - 1, j, cache) if i and val < matrix[i - 1][j] else 0
        a2 = self.dfs(matrix, m, n, i, j + 1, cache) if j + 1 < n and val < matrix[i][j + 1] else 0
        a3 = self.dfs(matrix, m, n, i + 1, j, cache) if i + 1 < m and val < matrix[i + 1][j] else 0
        a4 = self.dfs(matrix, m, n, i, j - 1, cache) if j and val < matrix[i][j - 1] else 0
        cache[i][j] = max(a1, a2, a3, a4) + 1
        return cache[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = [[0] * n for _ in range(m)]
        ans = 1
        for i in range(m):
            for j in range(n):
                tmp = self.dfs(matrix, m, n, i, j, cache)
                ans = max(ans, tmp)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    print(s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
    print(s.longestIncreasingPath([[1]]))
