class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        """
        Push element x onto queue_stack.
        """
        self.B.append(x)
        while self.A:
            self.B.append(self.A.pop(0))
        self.A, self.B = self.B, self.A

    def pop(self) -> int:
        """
        Removes the element on top of the queue_stack and returns that element.
        """
        return self.A.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.A[0]

    def empty(self) -> bool:
        """
        Returns whether the queue_stack is empty.
        """
        return not self.A

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
