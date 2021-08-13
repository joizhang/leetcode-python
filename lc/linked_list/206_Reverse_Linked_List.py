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

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归终止条件是当前为空，或者下一个节点为空
        if head is None or head.next is None:
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur


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
