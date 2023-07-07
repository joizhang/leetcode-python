from utils import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA


if __name__ == '__main__':
    s = Solution()
    headA = ListNode()
    headA.from_list([4, 1])
    headB = ListNode()
    headB.from_list([5, 6, 1, 8, 4, 5])
    headA.next.next = headB.next.next.next
    print(s.getIntersectionNode(headA, headB))
