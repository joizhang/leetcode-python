from typing import List

from utils import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        q = [root]
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if i == n - 1:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
