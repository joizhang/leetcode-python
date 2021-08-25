from typing import List


class Solution:
    """
    子序列（subsequence）：子序列并不要求连续，例如：序列 [4, 6, 5] 是 [1, 2, 4, 3, 7, 6, 5] 的一个子序列；
    子串（substring、subarray）：子串一定是原始字符串的连续子串。
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        n = len(nums)
        tails = [0] * n
        size = 0
        for num in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            if i == size:
                size += 1
        return size


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(s.lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))
