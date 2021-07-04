from utils import ListNode, list_to_linklist, linklist_to_list


class Solution:

    def reverse(self, head):
        if not head:
            return head
        p, cur = None, head
        while cur:
            head = head.next
            cur.next = p
            p = cur
            cur = head
        return p

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast, p = head, head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        slow.next = None

        q1 = head.next
        q2 = self.reverse(start)
        i = 0
        while q1 or q2:
            if i % 2 != 0 and q1:
                p.next = q1
                q1 = q1.next

            if i % 2 == 0 and q2:
                p.next = q2
                q2 = q2.next

            p = p.next
            i += 1


if __name__ == '__main__':
    s = Solution()
    l = list_to_linklist([1, 2, 3, 4])
    s.reorderList(l)
    print(linklist_to_list(l))

    l = list_to_linklist([1, 2, 3, 4, 5])
    s.reorderList(l)
    print(linklist_to_list(l))
