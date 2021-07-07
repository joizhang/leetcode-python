from utils import ListNode, TreeNode, list_to_linklist


class Solution:
    def build(self, arr, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        root = TreeNode(arr[mid])
        root.left = self.build(arr, start, mid - 1)
        root.right = self.build(arr, mid + 1, end)
        return root

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.build(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    s = Solution()
    l = list_to_linklist([-10, -3, 0, 5, 9])
    t = s.sortedListToBST(l)
