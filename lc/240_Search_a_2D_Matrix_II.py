from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = n - 1, 0
        while i >= 0 and j <= m - 1:
            if matrix[j][i] == target:
                return True
            elif matrix[j][i] > target:
                i -= 1
            else:
                j += 1
        return False