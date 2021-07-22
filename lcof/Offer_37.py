import collections

from utils import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue and i < len(vals):
            node = queue.popleft()
            if i < len(vals) and vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    t = codec.deserialize('[1,2,3,null,null,4,5]')
    print(codec.serialize(t))
