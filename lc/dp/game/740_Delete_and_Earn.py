from typing import List


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        在原来的 nums 的基础上构造一个临时的数组 all，这个数组，以元素的值来做下标，
        下标对应的元素是原来的元素的个数。这样就可以变成打家劫舍的问题
        :param nums:
        :return:
        """
        max_val = max(nums)
        tmp = [0] * (max_val + 1)
        for num in nums:
            tmp[num] += 1
        dp = [0] * (len(tmp) + 1)
        dp[1] = tmp[0]
        for i in range(1, len(tmp)):
            dp[i + 1] = max(
                dp[i],  # 不抢i处的
                dp[i - 1] + tmp[i] * i  # 抢i处的
            )
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.deleteAndEarn([3, 4, 2]))
    print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))
