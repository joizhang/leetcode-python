from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] 代表前 i 个房子在满足条件下的能偷窃到的最高金额。
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(1, n):
            # dp[n+1] = max(dp[n], dp[n−1] + num)
            dp[i + 1] = max(
                dp[i],  # 不抢i处的
                dp[i - 1] + nums[i],  # 抢i处的
            )
        return dp[-1]

    def rob2(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob2([1, 2, 3, 1]))
