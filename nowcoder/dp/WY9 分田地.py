# -*- coding: utf8 -*-

"""
横竖各三刀将一个矩阵分为16部分，每部分的value即为这一部分包含的所有数字之和。
我们要做的就是想一种切法，使得这16部分中value最小的那个尽可能的大。
首先很显然，每一个部分的value在0-sum之间，sum是指整个矩阵所有数字之和，
这样最终的结果一定是[0, sum]中的某一个整数。
这里稍微逆向思考一下，既然不容易直接求结果，可不可以我猜一个值k
然后判断能不能通过某种切法使最小的那一块value>=k,也就是说，使16块的value都能大于等于k,
如果可以的话，我们就可以对[0, sum]这个区间进行二分查找。
二分的复杂度是log(sum).
接下来是重点：对于一个值，怎么判断能不能横竖切三刀，使16块的value都大于等于k呢
二分答案，判断可行性时暴力枚举三列的情况，然后横着贪心地扫一遍,
每当四列都满足的时候就砍一刀，满足四次即可
"""
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append([int(s) for s in input()])
print(matrix)

sum_values = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_values[i][j] += sum_values[i - 1][j] + sum_values[i][j - 1] - sum_values[i - 1][j - 1] + matrix[i - 1][j - 1]


def calculate_sum(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    a1, a2 = sum_values[x1 - 1][y1 - 1], sum_values[x1 - 1][y2]
    a3, a4 = sum_values[x2][y1 - 1], sum_values[x2][y2]
    value = a4 - a3 - a2 + a1
    return value


def check(mid):
    for j1 in range(1, m - 2):
        if calculate_sum((1, 1), (n, j1)) < mid * 4:
            continue
        for j2 in range(j1 + 1, m - 1):
            if calculate_sum((1, j1 + 1), (n, j2)) < mid * 4:
                continue
            for j3 in range(j2 + 1, m):
                if calculate_sum((1, j2 + 1), (n, j3)) < mid * 4:
                    continue
                if calculate_sum((1, j3 + 1), (n, m)) < mid * 4:
                    continue
                pstart, row_count = 1, 0
                for pend in range(1, n + 1):
                    p1_list = [(pstart, 1), (pstart, j1 + 1), (pstart, j2 + 1), (pstart, j3 + 1)]
                    p2_list = [(pend, j1), (pend, j2), (pend, j3), (pend, m)]
                    values = [calculate_sum(p1, p2) for p1, p2 in zip(p1_list, p2_list)]
                    if min(values) >= mid:
                        pstart = pend + 1
                        row_count += 1
                        if row_count == 4:
                            return True
    return False


l, r = 0, sum_values[n][m]
answer = 0
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        l = mid + 1
        answer = mid
    else:
        r = mid - 1
print(answer)
