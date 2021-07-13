from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while True:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for i in reversed(range(left, right + 1)):
                ans.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break

            for i in reversed(range(top, bottom + 1)):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ans


if __name__ == '__main__':
    s = Solution2()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.spiralOrder(matrix))

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(s.spiralOrder(matrix))
