# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from utils import TreeNode, Codec


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        self.recur(root, targetSum, [], ans)
        return ans

    def recur(self, root, targetSum, track, ans):
        if not root:
            return
        if not root.left and not root.right and root.val == targetSum:
            track.append(root.val)
            ans.append(track.copy())
            track.pop()
            return
        track.append(root.val)
        self.recur(root.left, targetSum - root.val, track, ans)
        self.recur(root.right, targetSum - root.val, track, ans)
        track.pop()


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('5,4,8,11,null,13,4,7,2,null,null,5,1')
    print(s.pathSum(t, 22))
