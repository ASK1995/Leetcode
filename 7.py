class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if(x < 0):
            neg = True
            x *= -1
        rev_x = 0
        while(x != 0):
            rev_x = rev_x * 10 + x % 10
            x //= 10
        if(neg):
            rev_x *= -1
        if(rev_x > 2**31 - 1 or rev_x < -2**31):
            return 0
        return rev_x