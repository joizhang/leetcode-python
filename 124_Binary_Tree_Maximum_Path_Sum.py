# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = -sys.maxsize - 1

    def max_side(self, root: TreeNode):
        if root is None:
            return 0
        left_sum = max(0, self.max_side(root.left))
        right_sum = max(0, self.max_side(root.right))
        self.ans = max(self.ans, left_sum + right_sum + root.val)
        return max(left_sum, right_sum) + root.val

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_side(root)
        return self.ans


def list_to_tree(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None
    t = TreeNode(val=nums[index])
    t.left = list_to_tree(nums, index * 2 + 1)
    t.right = list_to_tree(nums, index * 2 + 2)
    return t


if __name__ == '__main__':
    s = Solution()
    print(s.maxPathSum(list_to_tree([1, 2, 3], 0)))
    print(s.maxPathSum(list_to_tree([-10, 9, 20, None, None, 15, 7], 0)))
