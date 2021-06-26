# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect_two_node(self, node1, node2):
        if node1 is None and node2 is None:
            return

        node1.next = node2
        self.connect_two_node(node1.left, node1.right)
        self.connect_two_node(node2.left, node2.right)
        self.connect_two_node(node1.right, node2.left)

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        self.connect_two_node(root.left, root.right)
        return root


def list_to_tree(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None
    t = Node(val=nums[index])
    t.left = list_to_tree(nums, index * 2 + 1)
    t.right = list_to_tree(nums, index * 2 + 2)
    return t


def tree_to_list(root: Node):
    nums = []
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        if node is not None:
            q.append(node.left)
            q.append(node.right)
            nums.append(node.val)
            if node.next is None:
                nums.append('#')

    return nums


if __name__ == '__main__':
    s = Solution()
    print(tree_to_list(s.connect(list_to_tree([1, 2, 3, 4, 5, 6, 7], 0))))
