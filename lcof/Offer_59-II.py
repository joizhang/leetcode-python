import collections
import queue


class MaxQueue:
    # 错误记录：我使用的是最大栈，当value大于max_stack[-1]才入栈，这个想法是错误的，比如push[1,4,5]，
    # 当5出栈后，4并没有在最大栈中
    def __init__(self):
        self.queue = queue.Queue()  # 队列
        self.deque = collections.deque()  # 双向队列

    def max_value(self) -> int:
        if not self.deque:
            return -1
        return self.deque[0]

    def push_back(self, value: int) -> None:
        self.queue.put(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)

    def pop_front(self) -> int:
        if self.queue.empty():
            return -1
        ans = self.queue.get()
        if self.deque[0] == ans:
            self.deque.popleft()
        return ans


if __name__ == '__main__':
    obj = MaxQueue()
    param_1 = obj.max_value()
    obj.push_back(1)
    param_3 = obj.pop_front()
