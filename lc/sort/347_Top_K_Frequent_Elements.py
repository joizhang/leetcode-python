import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        for a, b in collections.Counter(nums).items():
            bucket[b].append(a)
        res = []
        for arr in bucket[::-1]:
            if len(arr):
                res += arr
            if len(res) >= k:
                return res[:k]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
