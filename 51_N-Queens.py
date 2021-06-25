from copy import deepcopy
from typing import List


class Solution:

    def is_valid(self, board, row, col):
        n = len(board)
        # 检查列是否有皇后互相冲突
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        # 检查右上方是否有皇后互相冲突
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        # 检查左上方是否有皇后互相冲突
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        return True

    def backtrack(self, board, row, ans):
        if row == len(board):
            ans.append([''.join(x) for x in board])
            return

        n = len(board[row])
        for col in range(n):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1, ans)
            board[row][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        ans = []
        self.backtrack(board, 0, ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
