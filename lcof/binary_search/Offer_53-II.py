from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([0]))
    print(s.missingNumber([0, 2]))
    print(s.missingNumber([0, 1, 3]))
    print(s.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 9]))
