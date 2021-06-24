# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        temp = root.right
        root.right = root.left
        root.left = None

        p = root
        while p.right is not None:
            p = p.right
        p.right = temp
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
    print(tree_to_list(s.flatten(list_to_tree([1, 2, 5, 3, 4, None, 6], 0))))
