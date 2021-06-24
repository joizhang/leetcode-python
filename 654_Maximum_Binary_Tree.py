# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None
    t = TreeNode(val=nums[index])
    t.left = list_to_tree(nums, index * 2 + 1)
    t.right = list_to_tree(nums, index * 2 + 2)
    return t


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

    def max_index(self, nums: List[int], start, end):
        max_num, max_index = nums[start], start
        for i in range(start + 1, end):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index = i
        return max_index

    def recursive(self, nums: List[int], start, end):
        if start == end:
            return None
        max_index = self.max_index(nums, start, end)
        root = TreeNode(nums[max_index])
        root.left = self.recursive(nums, start, max_index)
        root.right = self.recursive(nums, max_index + 1, end)
        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.recursive(nums, 0, len(nums))


if __name__ == '__main__':
    s = Solution()
    print(tree_to_list(s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])))
