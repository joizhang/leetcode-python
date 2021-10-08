#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 求二叉树的右视图
# @param xianxu int整型一维数组 先序遍历
# @param zhongxu int整型一维数组 中序遍历
# @return int整型一维数组
#
from utils import TreeNode


class Solution:

    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return None
        inorder_root_idx = inorder.index(preorder[pre_start])
        root = TreeNode(preorder[pre_start])
        left_size = inorder_root_idx - in_start
        root.left = self.build(preorder, pre_start + 1, pre_start + left_size,
                               inorder, in_start, inorder_root_idx - 1)
        root.right = self.build(preorder, pre_start + left_size + 1, pre_end,
                                inorder, inorder_root_idx + 1, in_end)
        return root

    def build_tree(self, pre_order, in_order):
        return self.build(pre_order, 0, len(pre_order) - 1, in_order, 0, len(in_order) - 1)

    def solve(self, xianxu, zhongxu):
        # write code here
        root = self.build_tree(xianxu, zhongxu)
        ans, q = [], [root]
        while q:
            n = len(q)
            ans.append(q[n - 1].val)
            for _ in range(n):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.solve([1, 2, 4, 5, 3], [4, 2, 5, 1, 3]))
