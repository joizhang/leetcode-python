class ListNode:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if not self.table[index]:
            self.table[index] = ListNode(key, value)
        else:
            node = self.table[index]
            while True:
                if node.pair[0] == key:
                    node.pair = (key, value)
                    return
                if not node.next:
                    break
                node = node.next
            node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        node = self.table[index]
        while node:
            if node.pair[0] == key:
                return node.pair[1]
            else:
                node = node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        node = self.table[index]
        if not node:
            return
        elif node.pair[0] == key:
            self.table[index] = node.next
            return
        else:
            while node.next:
                if node.next.pair[0] == key:
                    node.next = node.next.next
                    return
                node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
