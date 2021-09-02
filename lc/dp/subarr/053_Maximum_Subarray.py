from typing import List


class Solution:
    """
    If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
    If the sum is negative, it has no use to the next element, so we break.
    it is a game of sum, not the elements.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

    def maxSubArray2(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
            ans = max(ans, dp[i])
            # print(dp)
        return ans

    def maxSubArray3(self, nums: List[int]) -> int:
        ans, dp = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp = nums[i] + max(dp, 0)
            ans = max(ans, dp)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray3([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
