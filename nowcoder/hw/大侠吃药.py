"""
5
2
4
2 1
3 1
4 2
1 5
"""
import collections

l = int(input())
m = int(input())
n = int(input())
pres = []
for i in range(n):
    pres.append(list(map(int, input().split())))
print(pres)

graph = {i + 1: set() for i in range(l)}
in_degrees = {i + 1: 0 for i in range(l)}

q = collections.deque()
# for in_degree in in_degrees.items():
#     if