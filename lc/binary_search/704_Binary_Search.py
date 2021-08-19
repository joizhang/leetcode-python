from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        # 注意是等于
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([1, 3, 5, 6], 5))
    print(s.search([1, 3, 5, 6], 2))
    print(s.search([1, 3, 5, 6], 7))
