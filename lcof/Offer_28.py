from utils import TreeNode, Codec


class Solution:
    def recur(self, left, right):
        if not left and not right:
            return True
        if (not left and right) or (left and not right) or left.val != right.val:
            return False
        return self.recur(left.left, right.right) and self.recur(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.recur(root.left, root.right)


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('1,2,2,None,3,None,3,None,None,None,None')
    print(s.isSymmetric(t))
