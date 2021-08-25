from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        ans = 0
        pre_max = values[0] + 0
        # 要求values[i] + values[j] + i - j最大
        for j in range(1, n):
            ans = max(ans, pre_max + values[j] - j)
            pre_max = max(pre_max, values[j] + j)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
    print(s.maxScoreSightseeingPair([1, 2]))
