from typing import List

from utils import TreeNode


class Solution:

    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start > pre_end:
            return None

        node = TreeNode(preorder[pre_start])
        inorder_root_index = inorder.index(preorder[pre_start])
        left_size = inorder_root_index - in_start
        node.left = self.build(preorder, pre_start + 1, pre_start + left_size,
                               inorder, in_start, inorder_root_index - 1)
        node.right = self.build(preorder, pre_start + left_size + 1, pre_end,
                                inorder, inorder_root_index + 1, in_end)
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
