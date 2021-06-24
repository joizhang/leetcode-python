# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_list(root: TreeNode):
    nums = []
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        if node is not None:
            q.append(node.left)
            q.append(node.right)
            nums.append(node.val)
    return nums


class Solution:

    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start > pre_end:
            return None
        inorder_root_index = inorder.index(preorder[pre_start])
        root = TreeNode(preorder[pre_start])
        left_size = inorder_root_index - in_start
        root.left = self.build(preorder, pre_start + 1, pre_start + left_size,
                               inorder, in_start, inorder_root_index - 1)
        root.right = self.build(preorder, pre_start + left_size + 1, pre_end,
                                inorder, inorder_root_index + 1, in_end)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


if __name__ == '__main__':
    s = Solution()
    print(tree_to_list(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
