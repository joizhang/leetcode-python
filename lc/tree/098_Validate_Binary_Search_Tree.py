# Definition for a binary tree node.
from utils import TreeNode, Codec


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
            if res[i] <= res[i - 1]:
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
    codec = Codec()
    print(s.isValidBST(codec.deserialize('2,1,3')))
    print(s.isValidBST(codec.deserialize('2,2,2')))
    print(s.isValidBST(codec.deserialize('5,1,4,None,None,3,6')))
    print(s.isValidBST(codec.deserialize('5,4,6,None,None,3,7')))
