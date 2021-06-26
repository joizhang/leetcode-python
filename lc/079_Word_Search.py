import sys
from typing import List


class Solution:
    directions = [(-1, 0), (0, 1), (1, 0), [0, -1]]
    m = 0
    n = 0
    visited = []

    def in_area(self, x, y):
        return (0 <= x < self.m) and (0 <= y < self.n)

    def backtrack(self, board, word, index, x, y):
        if index == len(word) - 1:
            return board[x][y] == word[index]

        if board[x][y] == word[index]:
            self.visited[x][y] = 1
            for d in self.directions:
                new_x, new_y = x + d[0], y + d[1]
                if self.in_area(new_x, new_y) \
                        and not self.visited[new_x][new_y] \
                        and self.backtrack(board, word, index + 1, new_x, new_y):
                    return True

            self.visited[x][y] = 0
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.visited = [[0] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if self.backtrack(board, word, 0, i, j):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
