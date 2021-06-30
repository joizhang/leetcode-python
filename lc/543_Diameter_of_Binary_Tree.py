from utils import TreeNode


class Solution:
    ans = 0

    def recur(self, root):
        if root is None:
            return 0
        left = self.recur(root.left)
        right = self.recur(root.right)
        self.ans = max(self.ans, left + right + 1)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.recur(root)
        return self.ans - 1
