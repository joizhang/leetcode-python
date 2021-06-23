# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def validBST(self, root: TreeNode, a):
        if root is None:
            return
        self.validBST(root.left, a)
        a.append(root.val)
        self.validBST(root.right, a)

    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.validBST(root, res)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        return True


def list_to_tree(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None
    t = TreeNode(val=nums[index])
    t.left = list_to_tree(nums, index * 2 + 1)
    t.right = list_to_tree(nums, index * 2 + 2)
    return t


if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST(list_to_tree([2, 1, 3], 0)))
    print(s.isValidBST(list_to_tree([2, 2, 2], 0)))
    print(s.isValidBST(list_to_tree([5, 1, 4, None, None, 3, 6], 0)))
    print(s.isValidBST(list_to_tree([5, 4, 6, None, None, 3, 7], 0)))
