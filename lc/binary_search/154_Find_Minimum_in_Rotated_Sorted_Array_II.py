from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[lo]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([2, 2, 2, 0, 1]))
    print(s.findMin([3, 3, 1, 3]))
    print(s.findMin([1, 3, 3]))
