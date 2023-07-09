from typing import List


class Solution:
    """
    剑指 Offer 66. 构建乘积数组
    """

    def constructArr(self, a: List[int]) -> List[int]:
        if not a:
            return []
        b = [1] * len(a)
        # 下三角
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]
        temp = 1
        for i in range(len(a) - 2, -1, -1):
            temp *= a[i + 1]
            b[i] *= temp
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.constructArr([1, 2, 3, 4, 5]))
