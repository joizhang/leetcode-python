from typing import Optional

from utils import TreeNode, Codec


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        return None if root.left == root.right and root.val == target else root


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('1,2,3,2,null,2,4')
    t = s.removeLeafNodes(t, 2)
    print(codec.serialize(t))
