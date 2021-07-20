from typing import List


class Solution:
    def rob_range(self, nums, start, end):
        cur, pre = 0, 0
        for num in nums[start:end + 1]:
            cur, pre = max(pre + num, cur), cur
        return cur

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            return max(self.rob_range(nums, 0, n - 2), self.rob_range(nums, 1, n - 1))


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2, 3, 2]))
