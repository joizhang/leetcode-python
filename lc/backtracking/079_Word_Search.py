from typing import List


class Solution:
    def dfs(self, board, m, n, word, index, i, j):
        if not 0 <= i < m or not 0 <= j < n or word[index] != board[i][j]:
            return False
        if index == len(word) - 1:
            return True
        board[i][j] = ''
        ans = self.dfs(board, m, n, word, index + 1, i - 1, j) or \
              self.dfs(board, m, n, word, index + 1, i, j + 1) or \
              self.dfs(board, m, n, word, index + 1, i + 1, j) or \
              self.dfs(board, m, n, word, index + 1, i, j - 1)
        # 注意还原
        board[i][j] = word[index]
        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, m, n, word, 0, i, j):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
