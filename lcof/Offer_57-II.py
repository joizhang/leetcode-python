from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        lo, hi, n = 1, 1, target // 2
        s = 1
        while lo <= n:
            if s < target:
                hi += 1
                s += hi
            elif s > target:
                s -= lo
                lo += 1
            else:
                ans.append([x for x in range(lo, hi + 1)])
                s -= lo
                lo += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findContinuousSequence(9))
    print(s.findContinuousSequence(15))
