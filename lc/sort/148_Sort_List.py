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

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge_two_list(left, right)


if __name__ == '__main__':
    s = Solution()
    l = list_to_linklist([4, 2, 1, 3])
    print(linklist_to_list(s.sortList(l)))
    l = list_to_linklist([-1, 5, 3, 4, 0])
    print(linklist_to_list(s.sortList(l)))
