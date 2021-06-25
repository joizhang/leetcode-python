# Definition for singly-linked list.
from utils import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        p = None
        cur = head
        while cur is not None:
            head = head.next
            cur.next = p
            p = cur
            cur = head
        return p


if __name__ == '__main__':
    s = Solution()
    linklist = list_to_linklist([1, 2, 3, 4, 5])
    print(linklist_to_list(linklist))
    reverse_linklist = s.reverseList(linklist)
    print(linklist_to_list(reverse_linklist))

    linklist = list_to_linklist([])
    print(linklist_to_list(linklist))
    reverse_linklist = s.reverseList(linklist)
    print(linklist_to_list(reverse_linklist))
