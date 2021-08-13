from typing import Optional

from utils import TreeNode, Codec


class Solution:
    sum = 0

    def recur(self, root):
        if not root:
            return
        self.recur(root.right)
        root.val += self.sum
        self.sum = root.val
        self.recur(root.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        self.recur(root)
        return root


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('4,1,6,0,2,5,7,null,null,null,3,null,null,null,8')
    t = s.convertBST(t)
    print(codec.serialize(t))
