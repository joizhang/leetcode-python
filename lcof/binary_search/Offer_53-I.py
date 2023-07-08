from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        ans = [-1, -1]
        if len(nums) == 0:
            return 0

        pos = self.find_fisrt_pos(nums, target)
        if pos == -1:
            return 0
        ans[0] = pos

        pos = self.find_last_pos(nums, target)
        ans[1] = pos
        return ans[1] - ans[0] + 1

    def find_fisrt_pos(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            # 偏左
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if nums[lo] == target:
            return lo
        return -1

    def find_last_pos(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            # 偏右
            mid = lo + (hi - lo + 1) // 2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        if nums[hi] == target:
            return hi
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([5, 7, 7, 8, 8, 10], 8))
    print(s.search([5, 7, 7, 8, 8, 10], 6))
