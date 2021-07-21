from typing import List

from utils import TreeNode, Codec


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = [root]
        height = 0
        while q:
            n, tmp = len(q), []
            for i in range(n):
                node = q.pop(0)
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if height % 2 != 0:
                tmp = tmp[::-1]
            height += 1
            ans.append(tmp)
        return ans


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('3,9,20,None,None,15,7,None,None,None,None')
    print(s.zigzagLevelOrder(t))
