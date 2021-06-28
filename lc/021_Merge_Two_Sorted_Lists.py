# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from utils import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        p = head
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return head


if __name__ == '__main__':
    s = Solution()
    l1 = list_to_linklist([1, 2, 4])
    l2 = list_to_linklist([1, 3, 4, 5, 6])
    print(linklist_to_list(s.mergeTwoLists(l1, l2)))
