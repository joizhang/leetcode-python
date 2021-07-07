from utils import TreeNode, Codec


class Solution:

    def count(self, root):
        if root is None:
            return 0
        left = self.count(root.left)
        right = self.count(root.right)
        return left + right + 1

    def countNodes(self, root: TreeNode) -> int:
        return self.count(root)


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    print(s.count(codec.deserialize('1,2,3,4,5,6,None,None,None,None,None,None,None')))
