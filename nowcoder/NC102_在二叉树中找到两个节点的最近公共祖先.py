# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root, o1, o2):
        # write code here
        if not root:
            return -1
        if root.val == o1 or root.val == o2:
            return root.val
        left = self.lowestCommonAncestor(root.left, o1, o2)
        right = self.lowestCommonAncestor(root.right, o1, o2)
        if left == -1:
            return right
        if right == -1:
            return left
        return root.val
