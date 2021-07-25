n = int(input())
A = list(map(int, input().split()))
i = len(A) - 1
# 最大的三个正数的乘积
while i >= len(A) - 3:
    is_sorted = False
    for j in range(0, i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            is_sorted = False
    if is_sorted:
        break
    i -= 1
# print(A)
ans1 = A[-1] * A[-2] * A[-3]
# 最小的两个负数*最大的正数的乘积
i = 0
while i <= 1:
    is_sorted = False
    for j in reversed(range(i + 1, len(A) - 3)):
        if A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            is_sorted = False
    if is_sorted:
        break
    i += 1
# print(A)
ans2 = A[0] * A[1] * A[-1]
print(max(ans1, ans2))
