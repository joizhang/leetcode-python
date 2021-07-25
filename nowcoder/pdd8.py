n = int(input())
nums = list(map(int, input().split()))

n = len(nums)
i = n - 1
while i >= n - 3:
    tmp = i
    for j in range(i):
        if nums[j] > nums[tmp]:
            tmp = j
    nums[tmp], nums[i] = nums[i], nums[tmp]
    i -= 1

i = 0
while i <= 1:
    tmp = i
    for j in range(i + 1, n):
        if nums[j] < nums[tmp]:
            tmp = j
    nums[tmp], nums[i] = nums[i], nums[tmp]
    i += 1

print(max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1]))
