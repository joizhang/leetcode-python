from utils import TreeNode, Codec


class Solution:

    def recursive(self, root):
        if root is None:
            return 0
        left = self.recursive(root.left)
        if left == -1:
            return -1
        right = self.recursive(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.recursive(root) != -1


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('3,9,20,None,None,15,7,None,None,None,None')
    print(s.isBalanced(t))
