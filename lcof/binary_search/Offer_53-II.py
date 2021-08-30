from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == mid:
                lo = mid + 1
            else:
                hi = mid
        return lo
