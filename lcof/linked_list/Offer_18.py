from utils import ListNode


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        p, q = head, head.next
        if p.val == val:
            return q
        while p and q:
            if q.val == val:
                p.next = q.next
                break
            p = p.next
            q = q.next
        return head


if __name__ == '__main__':
    s = Solution()
    l = ListNode()
    l.from_list([4, 5, 1, 9])
    l = s.deleteNode(l, 1)
    print(l.to_list())
