class OrderedStream:
    def __init__(self, n: int):
        self.arr = [""]* (n + 1)
        self.size = n + 1
        self.output = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey] = value
        res = []

        while(self.output < self.size and self.arr[self.output] != ""):
            res.append(self.arr[self.output])
            self.output += 1

        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)