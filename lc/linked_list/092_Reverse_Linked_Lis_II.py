from utils import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def reverse(self, head):
        if not head:
            return head
        p = None
        cur = head
        while head:
            head = head.next
            cur.next = p
            p = cur
            cur = head
        return p

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, end = dummy, dummy
        i = 0
        while i < left - 1:
            pre = pre.next
            i += 1
        i = 0
        while i < right:
            end = end.next
            i += 1

        start = pre.next
        end_next = end.next

        end.next = None
        pre.next = self.reverse(start)
        start.next = end_next

        return dummy.next


if __name__ == '__main__':
    s = Solution()
    l = list_to_linklist([1, 2, 3, 4, 5])
    print(linklist_to_list(s.reverseBetween(l, 2, 4)))
