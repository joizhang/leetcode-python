from typing import List

from utils import TreeNode, Codec


class Solution:
    def recur(self, root, track, ans):
        if not root:
            return
        if not root.left and not root.right:
            track.append(str(root.val))
            ans.append("->".join(track))
            track.pop()
            return
        track.append(str(root.val))
        self.recur(root.left, track, ans)
        self.recur(root.right, track, ans)
        track.pop()

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        self.recur(root, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('1,2,3,null,5')
    print(s.binaryTreePaths(t))
