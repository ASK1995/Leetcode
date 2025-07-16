class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while(n != 1):
            if(n % 2 == 0):
                n //= 2
            elif n != 3 and (n & 3 == 3):
                n += 1
            else:
                n = n - 1
            res += 1
        return res