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

    def build(self, inorder, in_start, in_end, postorder, post_start, post_end):
        if post_start > post_end:
            return None
        inorder_root_index = inorder.index(postorder[post_end])
        root = TreeNode(postorder[post_end])
        left_size = inorder_root_index - in_start
        root.left = self.build(inorder, in_start, inorder_root_index - 1,
                               postorder, post_start, post_start + left_size - 1)
        root.right = self.build(inorder, inorder_root_index + 1, in_end,
                                postorder, post_start + left_size, post_end - 1)
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)


if __name__ == '__main__':
    s = Solution()
    print(tree_to_list(s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])))
