from typing import List


class Solution:
    """
    只要数组中存在一个元素比相邻元素大，那么沿着它一定可以找到一个峰值
    """

    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
