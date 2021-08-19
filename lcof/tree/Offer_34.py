from typing import List

from utils import TreeNode, Codec


class Solution:
    def backtrack(self, root, target, track, ans):
        if not root:
            return
        track.append(root.val)
        target -= root.val
        if target == 0 and not root.left and not root.right:
            ans.append(track.copy())
        self.backtrack(root.left, target, track, ans)
        self.backtrack(root.right, target, track, ans)
        track.pop()

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ans = []
        self.backtrack(root, target, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('5,4,8,11,null,13,4,7,2,null,null,5,1,null,null,null,null')
    print(s.pathSum(t, 22))
