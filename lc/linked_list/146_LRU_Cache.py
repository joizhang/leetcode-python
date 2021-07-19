class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
        node = self.hashmap[key]
        # 将结点从链表中分离
        node.prev.next = node.next
        node.next.prev = node.prev
        # 将node插入到尾节点前
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_node_to_tail(key)
        else:
            # 缓存满，移除开头结点
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new = ListNode(key, value)
            self.hashmap[key] = new
            # 插入到链表开头
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new


if __name__ == '__main__':
    # Your LRUCache object will be instantiated and called as such:
    obj = LRUCache(2)
    obj.put(2, 1)
    obj.put(1, 1)
    obj.put(2, 3)
    obj.put(4, 1)
    print(obj.get(1))
    print(obj.get(2))
