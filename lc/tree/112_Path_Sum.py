from typing import Optional

from utils import TreeNode, Codec


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 出错点：但测试数据为[1,2], 1时错误，表示只有是叶子节点时才符合要求
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('5,4,8,11,null,13,4,7,2,null,null,null,1')
    print(s.hasPathSum(t, 22))

    t = codec.deserialize('1,2,3')
    print(s.hasPathSum(t, 5))

    t = codec.deserialize('1,2,null')
    print(s.hasPathSum(t, 0))

    t = codec.deserialize('1,2,null')
    print(s.hasPathSum(t, 1))
