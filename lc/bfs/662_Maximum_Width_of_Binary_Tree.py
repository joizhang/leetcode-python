from typing import Optional

from utils import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [(root, 0, 0)]
        cur_depth, left, ans = 0, 0, 0
        while q:
            node, depth, pos = q.pop(0)
            if node:
                q.append((node.left, depth + 1, pos * 2))
                q.append((node.right, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(ans, pos - left + 1)
        return ans
