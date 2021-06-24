# Definition for a binary tree node.
from typing import List

from utils import TreeNode, Codec


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
            dd[sub_tree] += 1
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
    codec = Codec()
    print(s.findDuplicateSubtrees(codec.deserialize('1,2,3,4,None,2,4,None,None,4,None,None,None')))
    # print(tree_list_to_list(s.findDuplicateSubtrees()))
