MOD = 99997867


def solve(n, d, nums):
    """
    暴力解法: dp[i] 以 nums[i] 为最大元素的方案数
    时间复杂度 0(n^2)
    """
    dp = [0] * n
    dp[2] = 1 if nums[2] - nums[0] <= d else 0
    for i in range(3, n):
        c = 0
        j = i - 1
        while j >= 0 and nums[j] + d >= nums[i]:
            c += 1
            j -= 1
        dp[i] += c * (c - 1) // 2 if c >= 3 else 0
        dp[i] %= MOD
    return sum(dp) % MOD


def solve2(n, d, nums):
    dp = [0] * n
    dp[2] = 1 if nums[2] - nums[0] <= d else 0
    j = 0
    for i in range(3, n):
        while j < i and nums[j] + d < nums[i]:
            j += 1
        c = i - j
        dp[i] += c * (c - 1) // 2 if c >= 3 else 0
        dp[i] %= MOD
    return sum(dp) % MOD


N, D = map(int, input().split())
nums = list(map(int, input().split()))
# print(nums)
print(solve(N, D, nums))
