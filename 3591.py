from collections import Counter

class Solution:
    def isPrime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, num, 2):
            if num % i == 0:
                return False
        return True

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for value in count.values():
            if(self.isPrime(value)):
                return True
        return False