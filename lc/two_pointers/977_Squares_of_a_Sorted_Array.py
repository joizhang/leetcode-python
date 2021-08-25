from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        lo, hi, k = 0, len(nums) - 1, len(nums) - 1
        while lo <= hi:
            if nums[lo] ** 2 > nums[hi] ** 2:
                ans[k] = nums[lo] ** 2
                lo += 1
            else:
                ans[k] = nums[hi] ** 2
                hi -= 1
            k -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-5, -3, -2, -1]))
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
    print(s.sortedSquares([-7, -3, 2, 3, 11]))
