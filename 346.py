class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.values = []
        self.total = 0

    def next(self, val: int) -> float:
        self.values.append(val)
        self.total += val
        if(len(self.values) > self.size):
            self.total -= self.values[0]
            self.values.pop(0)

        return self.total/len(self.values)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)