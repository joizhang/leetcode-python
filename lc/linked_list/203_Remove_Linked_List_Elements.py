from utils import *


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    linklist = list_to_linklist([1, 2, 6, 3, 4, 5, 6])
    print(linklist_to_list(s.removeElements(linklist, 6)))
