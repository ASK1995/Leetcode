class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        m = 2*n
        total = (m * (m + 1))//2
        odd = n * n
        even = total - odd

        def gcd(a, b):
            print(a, b)
            a, b = b, a % b
            if(b == 0):
                return a
            return gcd(a, b)

        return gcd(even, odd)