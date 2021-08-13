import collections
from typing import Optional

from utils import TreeNode, Codec


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([(1, root)])
        max_width = 0
        while q:
            n = len(q)
            min_col_width, _ = q[0]
            for _ in range(n):
                col_width, node = q.popleft()
                if node.left:
                    q.append((col_width * 2, node.left))
                if node.right:
                    q.append((col_width * 2 + 1, node.right))
            max_width = max(max_width, col_width - min_col_width + 1)
        return max_width


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('1,3,2,5,3,null,9')
    print(s.widthOfBinaryTree(t))

    t = codec.deserialize('1,3,null,5,3')
    print(s.widthOfBinaryTree(t))

    t = codec.deserialize('1,3,2,5,null')
    print(s.widthOfBinaryTree(t))

    t = codec.deserialize('1,3,2,5,null,null,9,6,null,null,7')
    print(s.widthOfBinaryTree(t))

