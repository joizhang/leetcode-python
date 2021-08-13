from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        i = 0
        while i < len(intervals):
            if intervals[i][0] > newInterval[0]:
                break
            i += 1
        intervals.insert(i, newInterval)

        ans = []
        newInterval = intervals[0]
        ans.append(newInterval)
        for interval in intervals:
            if interval[0] <= newInterval[1]:
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                newInterval = interval
                ans.append(newInterval)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.insert([[1, 3], [6, 9]], [2, 5]))
    print(s.insert([[1, 5]], [2, 7]))
