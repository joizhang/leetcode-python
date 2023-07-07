from utils import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
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


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode()
    l1.from_list([1, 2, 4])
    l2 = ListNode()
    l2.from_list([1, 3, 4])
    head = s.mergeTwoLists(l1, l2)
    print(head.to_list())
