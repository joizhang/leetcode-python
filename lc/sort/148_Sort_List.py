from utils import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def merge_two_list(self, l1: ListNode, l2: ListNode):
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

    def sortList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList2(head)
        right = self.sortList2(mid)
        return self.merge_two_list(left, right)

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        small, large = ListNode(-1), ListNode(-1)
        sp, lp = small, large
        cur = head.next
        while cur:
            if cur.val < head.val:
                sp.next = cur
                sp = sp.next
            else:
                lp.next = cur
                lp = lp.next
            cur = cur.next

        sp.next = None
        lp.next = None
        sp = self.sortList(small.next)
        lp = self.sortList(large.next)

        cur = sp
        if cur:
            while cur.next:
                cur = cur.next
            cur.next = head
            head.next = lp
            return sp
        else:
            head.next = lp
            return head


if __name__ == '__main__':
    s = Solution()
    l = list_to_linklist([4, 2, 1, 3])
    print(linklist_to_list(s.sortList2(l)))
    l = list_to_linklist([-1, 5, 3, 4, 0])
    print(linklist_to_list(s.sortList2(l)))

    l = list_to_linklist([4, 2, 1, 3])
    print(linklist_to_list(s.sortList(l)))
    l = list_to_linklist([-1, 5, 3, 4, 0])
    print(linklist_to_list(s.sortList(l)))
