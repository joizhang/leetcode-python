from utils import TreeNode, Codec


class Solution:
    k = 0
    res = 0

    def recur(self, root, k):
        if not root:
            return
        self.recur(root.right, k)
        if self.k == k:
            return
        self.k += 1
        if self.k == k:
            self.res = root.val
        self.recur(root.left, k)

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.recur(root, k)
        return self.res


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('3,1,4,None,2,None,None')
    print(s.kthLargest(t, 3))
