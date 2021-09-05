from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.generate(3))
    print(s.generate(4))
    print(s.generate(5))
