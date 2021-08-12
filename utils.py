SEP = ','
NONE = 'None'
NULL = 'null'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


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
            if left != NONE and left != NULL:
                parent.left = TreeNode(int(left))
                q.append(parent.left)
            else:
                parent.left = None
            # 父节点对应的右侧子节点的值
            right = nodes[i]
            i += 1
            if right != NONE and right != NULL:
                parent.right = TreeNode(int(right))
                q.append(parent.right)
            else:
                parent.right = None
        return root


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def list_to_linklist(nums):
    if len(nums) == 0:
        return None
    head = ListNode(val=nums[0])
    p = head
    for i in range(1, len(nums)):
        p.next = ListNode(val=nums[i])
        p = p.next
    return head


def linklist_to_list(head):
    nums = []
    p = head
    while p is not None:
        nums.append(p.val)
        p = p.next
    return nums
