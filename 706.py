class MyHashMap:
    def __init__(self):
        self.data = [-1]*(10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        val = self.data[key]
        if(val != -1):
            return val
        return -1

    def remove(self, key: int) -> None:
        self.data[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)