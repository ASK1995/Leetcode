class Solution:
    def gcd(self, a, b):
        if(a > b):
            a, b = b, a
        if(b % a == 0):
            return a
        return self.gcd(b % a, a)

    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(max(nums), min(nums))