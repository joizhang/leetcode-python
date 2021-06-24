# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


SEP = ','
NONE = 'None'


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        s = ''
        q = [root]
        while len(q) != 0:
            cur = q.pop(0)
            # 层级遍历代码位置
            if cur is None:
                s = s + SEP + NONE
                continue
            s = s + SEP + str(cur.val)

            q.append(cur.left)
            q.append(cur.right)
        return s if s == '' else s[1:]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = [root]
        i = 1
        while i < len(nodes):
            # 队列中存的都是父节点
            parent = q.pop(0)
            # 父节点对应的左侧子节点的值
            left = nodes[i]
            i += 1
            if left != NONE:
                parent.left = TreeNode(int(left))
                q.append(parent.left)
            else:
                parent.left = None
            # 父节点对应的右侧子节点的值
            right = nodes[i]
            i += 1
            if right != NONE:
                parent.right = TreeNode(int(right))
                q.append(parent.right)
            else:
                parent.right = None
        return root
