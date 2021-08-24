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

    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        # find the mid node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        node = self.reverse(slow)
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

