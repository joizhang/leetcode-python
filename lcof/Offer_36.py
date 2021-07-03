from utils import Node, Codec


class Solution:
    pre = None
    head = None

    def recursive(self, cur):
        if cur is None:
            return

        self.recursive(cur.left)

        if self.pre:
            self.pre.right, cur.left = cur, self.pre
        else:
            self.head = cur
        self.pre = cur

        self.recursive(cur.right)

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.recursive(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


if __name__ == '__main__':
    s = Solution()
    codec = Codec()
    t = codec.deserialize('4,2,5,1,3,None,None,None,None,None,None')
    print(s.treeToDoublyList(t))
