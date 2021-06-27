from utils import TreeNode, Codec


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('3,9,20,None,None,15,7,None,None,None,None')
    print(s.maxDepth(t))
