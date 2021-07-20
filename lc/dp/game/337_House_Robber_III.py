from utils import TreeNode


class Solution:
    def rob_internal(self, root):
        #  0 代表不偷，1 代表偷
        ans = [0, 0]
        if not root:
            return ans
        left = self.rob_internal(root.left)
        right = self.rob_internal(root.right)
        ans[0] = max(left[0], left[1]) + max(right[0], right[1])
        ans[1] = left[0] + right[0] + root.val
        return ans

    def rob(self, root: TreeNode) -> int:
        ans = self.rob_internal(root)
        return max(ans[0], ans[1])
