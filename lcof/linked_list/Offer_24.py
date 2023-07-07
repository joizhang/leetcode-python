from utils import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        p = head
        while head:
            head = head.next
            p.next = dummy.next
            dummy.next = p
            p = head
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode()
    head.from_list([1, 2, 3, 4, 5])
    reversed_head = s.reverseList(head)
    print(reversed_head.to_list())
