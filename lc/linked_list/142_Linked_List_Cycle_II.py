from utils import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return head
        slow, fast = head, head
        has_cycle = False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        if not has_cycle:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
