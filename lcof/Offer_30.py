class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or x <= self.B[-1]:
            self.B.append(x)

    def pop(self) -> None:
        if self.B[-1] == self.A[-1]:
            self.B.pop()
        self.A.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    print(obj.min())
