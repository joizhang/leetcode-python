from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        i, j,  = 1, 2
        s = i + j
        while i < j:
            if s == target:
                ans.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findContinuousSequence(9))
    print(s.findContinuousSequence(15))
