from typing import List


class Solution:
    def recur(self, postorder, start, end):
        if start >= end:
            return True
        i = start
        while postorder[i] < postorder[end]:
            i += 1
        mid = i
        while postorder[i] > postorder[end]:
            i += 1
        return i == end and self.recur(postorder, start, mid - 1) and self.recur(postorder, mid, end - 1)

    def verifyPostorder(self, postorder: List[int]) -> bool:
        return self.recur(postorder, 0, len(postorder) - 1)
