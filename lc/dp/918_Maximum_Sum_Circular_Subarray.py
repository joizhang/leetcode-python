from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        1 不使用环的情况时，直接通过53题的思路，逐步求出整个数组中的最大子序和即可
        2 使用到了环，则必定包含 A[n-1]和 A[0]两个元素且说明从A[1]到A[n-2]这个子数组中必定包含负数
        因此只需要把A[1]-A[n-2]间这些负数的最小和求出来
        用整个数组的和 sum减掉这个负数最小和即可实现原环型数组的最大和
        最后再比较直接通过53题思路求出无环子序列和用sum-min的有环子序列比较大小求出整个数组的最大值即可！

        作者：lizhihua2034
        链接：https://leetcode-cn.com/problems/maximum-sum-circular-subarray/solution/java-dp-kan-bu-dong-wei-shi-yao-sum-min-x7q53/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        dp = nums[0]
        max_val = dp
        sum_val = dp

        # 求最大子序列和
        for i in range(1, len(nums)):
            sum_val += nums[i]
            dp = nums[i] + max(dp, 0)
            max_val = max(max_val, dp)

        min_val = 0
        dp = nums[0]
        for i in range(1, len(nums) - 1):
            dp = nums[i] + min(dp, 0)
            min_val = min(min_val, dp)
        return max(max_val, sum_val - min_val)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarraySumCircular([1, -2, 3, -2]))
    print(s.maxSubarraySumCircular([5, -3, 5]))
    print(s.maxSubarraySumCircular([3, -1, 2, -1]))
    print(s.maxSubarraySumCircular([3, -2, 2, -3]))
    print(s.maxSubarraySumCircular([-2, -3, -1]))
