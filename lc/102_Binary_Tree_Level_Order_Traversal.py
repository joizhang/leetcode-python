from typing import List

from utils import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = [root]
        while q:
            n = len(q)
            temp = []
            for _ in range(n):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(temp)
        return ans
