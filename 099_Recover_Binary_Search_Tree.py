# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.recoverTree(root.left)
        self.recoverTree(root.right)
        # if root.left is not None and root.val < :


def list_to_tree(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None
    t = TreeNode(val=nums[index])
    t.left = list_to_tree(nums, index * 2 + 1)
    t.right = list_to_tree(nums, index * 2 + 2)
    return t


if __name__ == '__main__':
    s = Solution()
    print(s.recoverTree(list_to_tree([2, 1, 3], 0)))
    print(s.recoverTree(list_to_tree([2, 2, 2], 0)))
    print(s.recoverTree(list_to_tree([5, 1, 4, None, None, 3, 6], 0)))
    print(s.recoverTree(list_to_tree([5, 4, 6, None, None, 3, 7], 0)))
