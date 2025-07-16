class MinStack:
    def __init__(self):
        self.l = []
        self.min_l = []

    def push(self, val: int) -> None:
        self.l.append(val)
        min_val = min(val, self.min_l[-1] if self.min_l else val)
        self.min_l.append(min_val)

    def pop(self) -> None:
        self.l.pop()
        self.min_l.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.min_l[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()