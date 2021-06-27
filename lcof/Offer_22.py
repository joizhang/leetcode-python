from utils import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = q = head
        n = k
        while n > 0:
            p = p.next
            n -= 1

        while p:
            p = p.next
            q = q.next
        return q
