# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from utils import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = l1
        move = dummy
        extra = 0
        while l1 or l2 or extra:
            if l1 and l2:
                summary = l1.val + l2.val + extra
                l1.val = summary % 10
                extra = summary // 10
                move.next = l1
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                summary = l1.val + extra
                l1.val = summary % 10
                extra = summary // 10
                move.next = l1
                l1 = l1.next
            elif l2 and not l1:
                summary = l2.val + extra
                l2.val = summary % 10
                extra = summary // 10
                move.next = l2
                l2 = l2.next
            else:
                move.next = ListNode(extra)
                extra = extra // 10
            move = move.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    la = list_to_linklist([9, 9, 9, 9, 9, 9, 9])
    lb = list_to_linklist([9, 9, 9, 9])
    print(linklist_to_list(s.addTwoNumbers(la, lb)))
