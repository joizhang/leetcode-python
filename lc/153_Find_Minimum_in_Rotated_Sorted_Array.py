from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        """若 nums[left] <= nums[mid]，说明区间[left, mid]连续递增，则最小元素一定不在这个区间里，可以直接排除。"""
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= nums[lo] >= nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([1, 2, 3, 4, 5]))
    print(s.findMin([3, 4, 5, 1, 2]))
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(s.findMin([11, 13, 15, 17]))
    print(s.findMin([2, 3, 4, 5, 1]))
