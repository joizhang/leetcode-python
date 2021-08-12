from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(max_prod * nums[i], min_prod * nums[i], nums[i])
            y = min(max_prod * nums[i], min_prod * nums[i], nums[i])
            max_prod, min_prod = x, y
            ans = max(ans, max_prod)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))
    print(s.maxProduct([0, -2, 0, -2, 0, -1]))
