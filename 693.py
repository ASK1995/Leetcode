class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        one = (n%2 != 0)
        while(n != 0):
            digit = True if n % 2 == 1 else False
            if(digit == one):
                one = not one
            else:
                return False
            n //= 2
        return True