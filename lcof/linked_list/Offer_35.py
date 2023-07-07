"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from utils import Node


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        dd = {}
        cur = head
        while cur:
            dd[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            dd[cur].next = dd.get(cur.next)
            dd[cur].random = dd.get(cur.random)
            cur = cur.next
        return dd[head]
