import collections
from typing import List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def construct_graph(adj_list: List[List[int]]):
    node_count = len(adj_list)
    node_list = [Node(x + 1) for x in range(node_count)]
    for i in range(len(adj_list)):
        for j in range(len(adj_list[0])):
            tmp = node_list[adj_list[i][j] - 1]
            node_list[i].neighbors.append(tmp)
    return node_list[0]


class Solution:
    def dfs(self, node, lookup):
        if not node:
            return
        if node in lookup:
            return lookup[node]
        clone = Node(node.val, [])
        lookup[node] = clone
        for n in node.neighbors:
            clone.neighbors.append(self.dfs(n, lookup))
        return clone

    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}
        return self.dfs(node, lookup)

    def bfs(self, node, lookup):
        if not node:
            return
        clone = Node(node.val, [])
        lookup[node] = clone
        queue = collections.deque()
        queue.append(node)
        while queue:
            tmp = queue.popleft()
            for n in tmp.neighbors:
                if n not in lookup:
                    lookup[n] = Node(n.val, [])
                    queue.append(n)
                lookup[tmp].neighbors.append(lookup[n])
        return clone

    def cloneGraph2(self, node: 'Node') -> 'Node':
        lookup = {}
        return self.bfs(node, lookup)


if __name__ == '__main__':
    s = Solution()
    list1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph = construct_graph(list1)
    s.cloneGraph()
