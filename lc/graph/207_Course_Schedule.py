import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct graph
        graph = {i: set() for i in range(numCourses)}
        in_degrees = {i: 0 for i in range(numCourses)}

        for prerequisite in prerequisites:
            graph[prerequisite[1]].add(prerequisite[0])
            in_degrees[prerequisite[0]] += 1

        q = collections.deque()
        visited = set()

        for i, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(i)

        while q:
            i = q.popleft()
            visited.add(i)
            for g in graph[i]:
                in_degrees[g] -= 1
                if in_degrees[g] == 0:
                    q.append(g)
        return len(visited) == numCourses


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))
    print(s.canFinish(2, [[1, 0], [0, 1]]))
