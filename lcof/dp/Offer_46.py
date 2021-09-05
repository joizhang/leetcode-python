class Solution:
    def translateNum(self, num: int) -> int:
        nums = str(num)
        n = len(str(nums))
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            if nums[i - 2] == '1' or (nums[i - 2] == '2' and nums[i - 1] < '6'):
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]
        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.translateNum(12258))
