from utils import ListNode, list_to_linklist, linklist_to_list


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
    l = list_to_linklist([4, 5, 1, 9])
    l = s.deleteNode(l, 1)
    print(linklist_to_list(l))
