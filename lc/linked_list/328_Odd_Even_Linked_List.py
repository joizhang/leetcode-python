from utils import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head


if __name__ == '__main__':
    s = Solution()
    linklist = ListNode()
    linklist.from_list([1, 2, 3, 4, 5])
    linklist = s.oddEvenList(linklist)
    print(linklist.to_list())

    linklist = ListNode()
    linklist.from_list([2, 1, 3, 5, 6, 4, 7])
    linklist = s.oddEvenList(linklist)
    print(linklist.to_list())
