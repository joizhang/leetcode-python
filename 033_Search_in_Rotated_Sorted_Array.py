from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[lo]:  # 左边递增
                if nums[mid] >= target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # 右边递增
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(s.search([1], 0))
    print(s.search([1, 3], 3))
    print(s.search([5, 1, 3], 5))
