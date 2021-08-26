num = float(input())
if num == 0:
    print(0)
else:
    # 考虑小于1以及负数的情况
    if num > 0:
        sig = 1
    else:
        sig = -1
    num = abs(num)

    if num > 1:
        start, end = 1, num
    else:
        start, end = num, 1

    mid = (start + end) / 2
    while abs(mid ** 3 - num) > 0.001:
        if mid ** 3 > num:
            end = mid
        else:
            start = mid
        mid = (start + end) / 2
    print(round(sig * mid, 1))
