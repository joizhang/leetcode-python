from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [0] * (rowIndex + 1)
        ans[0] = 1
        for i in range(1, rowIndex + 1):
            for j in reversed(range(1, i + 1)):
                ans[j] += ans[j - 1]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))
    print(s.getRow(4))
    print(s.getRow(5))
