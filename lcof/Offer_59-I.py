import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        if not nums or len(nums) < k:
            return ans
        deque = collections.deque()
        for i in range(k):
            if not deque or nums[i] <= deque[-1]:
                deque.append(nums[i])
            else:
                while deque and nums[i] > deque[-1]:
                    deque.pop()
                deque.append(nums[i])
        ans.append(deque[0])

        for i in range(1, len(nums) - k + 1):
            if nums[i - 1] == deque[0]:
                deque.popleft()
            if not deque or nums[i + k - 1] <= deque[-1]:
                deque.append(nums[i + k - 1])
            else:
                while deque and nums[i + k - 1] > deque[-1]:
                    deque.pop()
                deque.append(nums[i + k - 1])
            ans.append(deque[0])

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(s.maxSlidingWindow([1, -1], 1))
