from typing import List


class Solution:
    def dfs(self, board, m, n, i, j, word, k):
        if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        board[i][j] = ""
        ans = self.dfs(board, m, n, i - 1, j, word, k + 1) or \
              self.dfs(board, m, n, i, j + 1, word, k + 1) or \
              self.dfs(board, m, n, i + 1, j, word, k + 1) or \
              self.dfs(board, m, n, i, j - 1, word, k + 1)
        board[i][j] = word[k]
        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, m, n, i, j, word, 0):
                    return True
        return False
