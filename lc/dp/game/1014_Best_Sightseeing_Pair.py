from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        ans = 0
        # 要求 values[i] + values[j] + i - j 最大
        # 变量 pre_max 记录当前元素 A[j] 之前的 A[i] + i 的最大值
        pre_max = values[0] + 0
        for j in range(1, n):
            ans = max(ans, pre_max + values[j] - j)
            pre_max = max(pre_max, values[j] + j)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
    print(s.maxScoreSightseeingPair([1, 2]))
