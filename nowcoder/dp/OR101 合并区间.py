intervals = [list(map(int, s.split(','))) for s in input().split()]
intervals.sort()
# print(intervals)
new_interval = intervals[0]
ans = []
for i in range(1, len(intervals)):
    interval = intervals[i]
    if interval[0] <= new_interval[1]:
        # 易错点
        new_interval[1] = max(new_interval[1], interval[1])
    else:
        ans.append(",".join([str(i) for i in new_interval]))
        new_interval = interval
ans.append(",".join([str(i) for i in new_interval]))
print(" ".join(ans))
