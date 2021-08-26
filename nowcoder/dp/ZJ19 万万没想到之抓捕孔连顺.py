MOD = 99997867


def solve(n, d, nums):
    """
    暴力解法: dp[i] 以 nums[i] 为最大元素的方案数
    时间复杂度 0(n^2)
    """
    dp = [0] * n
    dp[2] = 1 if nums[2] - nums[0] <= d else 0
    for i in range(3, n):
        count = 0
        j = i - 1
        while j >= 0 and nums[i] - nums[j] <= d:
            count += 1
            j -= 1
        dp[i] += count * (count - 1) // 2 if count >= 3 else 0
        dp[i] %= MOD
    return sum(dp) % MOD


def solve2(n, d, nums):
    """
    改进算法,nums是递增的,j不用每次都重新计算,类似滑动窗口
    dp[i]: 以nums[i]为最大元素的方案数
    i: 遍历到的数字
    j: 与i相差距离>d的最近的坐标索引
    时间复杂度O(n) ac
    """
    dp = [0] * n
    dp[2] = 1 if nums[2] - nums[0] <= d else 0
    j = 0
    for i in range(3, n):
        while j < i and nums[i] - nums[j] > d:
            j += 1
        count = i - j
        dp[i] += count * (count - 1) // 2 if count >= 3 else 0
        dp[i] %= MOD
    return sum(dp) % MOD


N, D = map(int, input().split())
nums = list(map(int, input().split()))
# print(nums)
print(solve2(N, D, nums))
