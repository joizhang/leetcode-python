# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, root: TreeNode):
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.traverse(root.left)
        self.traverse(root.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root


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


if __name__ == '__main__':
    s = Solution()
    # print(tree_to_list(list_to_tree([4,2,7,1,3,6,9], 0)))
    print(tree_to_list(s.invertTree(list_to_tree([4, 2, 7, 1, 3, 6, 9], 0))))
    print(tree_to_list(s.invertTree(list_to_tree([2, 1, 3], 0))))
