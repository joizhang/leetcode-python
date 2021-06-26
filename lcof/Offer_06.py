from typing import List

from utils import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        if head is None:
            return ans
        p = head
        while p is not None:
            ans.append(p.val)
            p = p.next
        return ans[::-1]
