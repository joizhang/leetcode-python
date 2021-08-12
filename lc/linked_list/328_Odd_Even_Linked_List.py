from utils import ListNode, list_to_linklist, linklist_to_list


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
    linklist = list_to_linklist([1, 2, 3, 4, 5])
    print(linklist_to_list(s.oddEvenList(linklist)))

    linklist = list_to_linklist([2, 1, 3, 5, 6, 4, 7])
    print(linklist_to_list(s.oddEvenList(linklist)))
