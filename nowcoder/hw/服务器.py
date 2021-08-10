"""
4
0,2,200,0,1
1,3,400,0,1
2,3,400,1,0
3,3,300,0,1
3 1 3 200 0 1
"""
m = int(input())
servers = []
for i in range(m):
    # 编号，cpu数，内存大小， 架构， 是否支持NP卡
    servers.append(list(map(int, input().split(','))))
# 服务器数， 选择策略， cpu数，内存大小，架构， NP
require = list(map(int, input().split()))
# print(m)
# print(servers)
# print(require)

servers.sort()

