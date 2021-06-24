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


def tree_list_to_list(roots):
    ans = []
    for root in roots:
        ans.append(tree_to_list(root))
    return ans


class Solution:

    def traverse(self, root, ans, dd):
        if root is None:
            return '#'

        left = self.traverse(root.left, ans, dd)
        right = self.traverse(root.right, ans, dd)
        sub_tree = str(left) + ',' + str(right) + ',' + str(root.val)

        if sub_tree not in dd:
            dd[sub_tree] = 1
        elif dd[sub_tree] == 1:
            ans.append(root)
        else:
            dd[sub_tree] += 1

        return sub_tree

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        ans = []
        dd = {}
        self.traverse(root, ans, dd)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(tree_to_list(list_to_tree([1, 2, 3, 4, None, 2, 4, None, None, 4], 0)))
    # print(tree_list_to_list(s.findDuplicateSubtrees()))
