from utils import ListNode


class Solution:
    def reverse(self, head):
        if not head:
            return head
        p, cur = None, head
        while cur:
            head = head.next
            cur.next = p
            p = cur
            cur = head
        return p

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, end = dummy, dummy
        while end.next:
            i = 1
            while i <= k and end:
                end = end.next
                i += 1
            if not end:
                break
            # 截取中间链
            start = pre.next
            end_next = end.next
            end.next = None
            # 翻转
            pre.next = self.reverse(start)
            start.next = end_next

            pre = start
            end = start
        return dummy.next
