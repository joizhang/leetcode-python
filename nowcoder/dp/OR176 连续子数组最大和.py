N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
# print(nums)
dp, ans = nums[0], nums[0]
for i in range(1, N):
    dp = nums[i] + max(dp, 0)
    ans = max(ans, dp)
print(ans)
