from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n):
            dp[i] = max(
                nums[i - 1] + dp[i - 2],  # 抢当前的
                dp[i - 1]                 # 不抢当前的
            )
        return dp[-1]
