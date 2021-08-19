from typing import List

from utils import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = [root]
        flag = 1
        while len(q) != 0:
            tmp = []
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(tmp[::flag])
            flag *= -1
        return ans
