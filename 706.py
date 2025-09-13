class MyHashMap:
    def __init__(self):
        self.key = [None]*1000001

    def put(self, key: int, value: int) -> None:
        self.key[key] = value

    def get(self, key: int) -> int:
        return self.key[key] if self.key[key] != None else -1

    def remove(self, key: int) -> None:
        self.key[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)