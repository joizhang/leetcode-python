from typing import List

from utils import TreeNode, Codec


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = [root]
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
            ans.append(tmp)
        return ans


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('3,9,20,null,null,15,7,null,null,null,null')
    print(s.levelOrder(t))
