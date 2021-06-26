from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid + 1 <= len(nums) - 1 and nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(s.findMin([11, 13, 15, 17]))
    print(s.findMin([2, 3, 4, 5, 1]))
