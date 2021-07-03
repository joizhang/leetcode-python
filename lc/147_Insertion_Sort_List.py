from utils import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        helper = ListNode(0)
        pre = helper
        cur = head
        while cur:
            next = cur.next
            while pre.next and cur.val > pre.next.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = helper
            cur = next
        return helper.next


if __name__ == '__main__':
    s = Solution()
    l = list_to_linklist([4, 2, 1, 3])
    print(linklist_to_list(s.insertionSortList(l)))