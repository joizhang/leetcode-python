from utils import *


class Solution:
    def reverse(self, head: ListNode):
        if not head:
            return head
        p, cur = None, head
        while cur:
            head = head.next
            cur.next = p
            p = cur
            cur = head
        return p

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        dummy = ListNode()
        move = dummy
        extra = 0
        while l1 or l2 or extra:
            if l1 and l2:
                summation = l1.val + l2.val + extra
                l1.val = summation % 10
                extra = summation // 10
                move.next = l1
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                summation = l1.val + extra
                l1.val = summation % 10
                extra = summation // 10
                move.next = l1
                l1 = l1.next
            elif not l1 and l2:
                summation = l2.val + extra
                l2.val = summation % 10
                extra = summation // 10
                move.next = l2
                l2 = l2.next
            else:
                node = ListNode(extra)
                extra = extra // 10
                move.next = node
            move = move.next
        return self.reverse(dummy.next)


if __name__ == '__main__':
    s = Solution()
    l1 = list_to_linklist([7, 2, 4, 3])
    l2 = list_to_linklist([5, 6, 4])
    l3 = s.addTwoNumbers(l1, l2)
    print(linklist_to_list(l3))

    l1 = list_to_linklist([5])
    l2 = list_to_linklist([5])
    l3 = s.addTwoNumbers(l1, l2)
    print(linklist_to_list(l3))
