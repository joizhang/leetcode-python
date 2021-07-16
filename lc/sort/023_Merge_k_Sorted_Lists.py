from typing import List

from utils import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(0)
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
        # 注意终止条件
        if lo == hi:
            return lists[lo]
        mid = lo + (hi - lo) // 2
        l1 = self.merge(lists, lo, mid)
        l2 = self.merge(lists, mid + 1, hi)
        return self.merge_two_lists(l1, l2)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge(lists, 0, len(lists) - 1)


if __name__ == '__main__':
    s = Solution()
    la = list_to_linklist([1, 4, 5])
    lb = list_to_linklist([1, 3, 4])
    lc = list_to_linklist([2, 6])
    ll = [la, lb, lc]
    print(linklist_to_list(s.mergeKLists(ll)))
