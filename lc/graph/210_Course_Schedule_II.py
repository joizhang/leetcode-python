import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        graph = {course: set() for course in range(numCourses)}
        in_degrees = {course: 0 for course in range(numCourses)}

        for prerequisite in prerequisites:
            graph[prerequisite[1]].add(prerequisite[0])
            in_degrees[prerequisite[0]] += 1

        q, visited = collections.deque(), set()
        for course, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(course)

        while q:
            course = q.popleft()
            if course not in visited:
                ans.append(course)
            visited.add(course)
            for g in graph[course]:
                in_degrees[g] -= 1
                if in_degrees[g] == 0:
                    q.append(g)

        return ans if len(visited) == numCourses else []


if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(2, [[1, 0]]))
    print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(s.findOrder(1, []))
