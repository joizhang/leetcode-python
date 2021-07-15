from utils import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return head


if __name__ == '__main__':
    s = Solution()
    l = list_to_linklist([1, 2, 3, 3, 4, 4, 5])
    print(linklist_to_list(s.deleteDuplicates(l)))
