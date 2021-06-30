from utils import TreeNode


class Solution:
    def recur(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.recur(root1.left, root2.left)
        root1.right = self.recur(root1.right, root2.right)
        return root1

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        return self.recur(root1, root2)
