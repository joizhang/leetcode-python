from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        connected = [[False] * numCourses for i in range(numCourses)]

        for i, j in prerequisites:
            connected[i][j] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])

        return [connected[i][j] for i, j in queries]
