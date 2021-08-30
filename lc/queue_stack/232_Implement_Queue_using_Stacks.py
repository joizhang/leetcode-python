class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.A.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.A and not self.B:
            return -1
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        return self.B.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.A and not self.B:
            return -1
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        return self.B[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.A and not self.B


if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    print(obj.empty())
    obj.push(1)
    print(obj.empty())
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
