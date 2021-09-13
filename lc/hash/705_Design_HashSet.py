class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = [None] * self.size

    def add(self, key: int) -> None:
        index = key % self.size
        node = self.table[index]
        if not node:
            self.table[index] = ListNode(key)
            return
        while True:
            if node.key == key:
                return
            if not node.next:
                break
            node = node.next
        node.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % self.size
        node = self.table[index]
        if not node:
            return
        elif node.key == key:
            self.table[index] = node.next
            return
        else:
            while node.next:
                if node.next.key == key:
                    node.next = node.next.next
                    return
                node = node.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size
        node = self.table[index]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
