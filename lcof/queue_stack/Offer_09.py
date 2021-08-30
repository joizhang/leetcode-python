class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        if not self.stack_in:
            return -1
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()


if __name__ == '__main__':
    # Your CQueue object will be instantiated and called as such:
    obj = CQueue()
    obj.appendTail(3)
    print(obj.deleteHead())
    print(obj.deleteHead())
