from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        ans = []
        new_interval = intervals[0]
        ans.append(new_interval)
        for interval in intervals:
            if interval[0] <= new_interval[1]:
                new_interval[1] = max(new_interval[1], interval[1])
            else:
                new_interval = interval
                ans.append(new_interval)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
