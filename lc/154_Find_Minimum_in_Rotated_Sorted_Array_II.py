from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            while lo < mid:
                if nums[lo] != nums[hi]:
                    break
                lo += 1
            if nums[mid] >= nums[lo] >= nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([2, 2, 2, 0, 1]))
    print(s.findMin([3, 3, 1, 3]))
    print(s.findMin([1, 3, 3]))
