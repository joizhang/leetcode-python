from utils import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p, q = headA, headB
        while p != q:
            if p:
                p = p.next
            else:
                p = headB

            if q:
                q = q.next
            else:
                q = headA
        return p
