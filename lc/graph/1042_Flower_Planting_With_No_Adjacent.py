from collections import defaultdict
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans = [0] * n
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        for u in range(1, n + 1):
            colors = set(range(1, 5)) - set(ans[v - 1] for v in graph[u])
            ans[u - 1] = colors.pop()
        return ans
