from utils import TreeNode


class Solution:

    def recur(self, A, B):
        # 当节点B为空：说明树B已匹配完成（越过叶子节点），因此返回true；
        if not B:
            return True
        # 当节点A为空：说明已经越过树A叶子节点，即匹配失败，返回false；
        # 当节点A和B的值不同：说明匹配失败，返回false
        if not A or A.val != B.val:
            return False
        # 判断A和B的左子节点是否相等
        # 判断A和B的右子节点是否相等
        return self.recur(A.left, B.left) and self.recur(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
