import bisect
from collections import Counter

class TwoSum:
    def __init__(self):
        self.nums = []
        self.count = Counter()

    def add(self, number: int) -> None:
        index = bisect.bisect_left(self.nums, number)
        self.nums.insert(index, number)

    def find(self, value: int) -> bool:
        i, j = 0, len(self.nums) - 1
        while(i < j):
            total = self.nums[i] + self.nums[j]
            if(total == value):
                return True
            elif(total > value):
                j -= 1
            else:
                i += 1
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)