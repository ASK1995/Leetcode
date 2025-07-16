from collections import Counter

class Solution:
    def isPrime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, n, 2):
            if(n % i == 0):
                return False
        return True

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for key, value in count.items():
            if(self.isPrime(value)):
                return True
        return False