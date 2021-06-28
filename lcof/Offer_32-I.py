from typing import List

from utils import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        q = [root]
        while len(q) != 0:
            node = q.pop(0)
            ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
