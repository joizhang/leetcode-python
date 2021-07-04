from utils import ListNode


class Solution:
    def reverse(self, head):
        if not head:
            return head
        p = None
        cur = head
        while head:
            head = head.next
            cur.next = p
            p = cur
            cur = head
        return p

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, end = dummy, dummy
        i = 0
        while i < left - 1:
            pre = pre.next
            i += 1
        i = 0
        while i < right:
            end = end.next
            i += 1

        start = pre.next
        end_next = end.next

        end.next = None
        pre.next = self.reverse(start)
        start.next = end_next

        return dummy.next