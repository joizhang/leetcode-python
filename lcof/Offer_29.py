from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while True:
            for i in range(l, r + 1):
                ans.append(matrix[t][i])
            t += 1
            if t > b:
                break

            for i in range(t, b + 1):
                ans.append(matrix[i][r])
            r -= 1
            if l > r:
                break

            for i in reversed(range(l, r + 1)):
                ans.append(matrix[b][i])
            b -= 1
            if t > b:
                break

            for i in reversed(range(t, b + 1)):
                ans.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return ans


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.spiralOrder(matrix))

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(s.spiralOrder(matrix))
