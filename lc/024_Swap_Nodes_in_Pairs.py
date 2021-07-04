from utils import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        while first.next and first.next.next:
            first = first.next.next
            second.next = first
            head.next = first.next
            first.next = head
            first = head
            second = first
            head = head.next
        return dummy.next