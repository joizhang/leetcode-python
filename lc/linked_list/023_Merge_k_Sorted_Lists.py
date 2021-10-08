# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_two_list(self, l1, l2):
        dummy = ListNode()
        move = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2
        return dummy.next

    def merge(self, lists, lo, hi):
        if lo == hi:
            return lists[lo]
        mid = (lo + hi) // 2
        l1 = self.merge(lists, lo, mid)
        l2 = self.merge(lists, mid + 1, hi)
        return self.merge_two_list(l1, l2)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.merge(lists, 0, len(lists) - 1)