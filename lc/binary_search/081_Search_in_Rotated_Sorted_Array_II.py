from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True
            while lo < mid:
                if nums[lo] != nums[mid]:
                    break
                lo += 1
            if nums[lo] <= nums[mid]:  # 左边递增
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # 右边递增
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.search([2, 5, 6, 0, 0, 1, 2], 0))
    print(s.search([2, 5, 6, 0, 0, 1, 2], 3))
