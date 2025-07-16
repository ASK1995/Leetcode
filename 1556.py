class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = ""
        i = 0
        if(n == 0):
            return "0"

        while(n != 0):
            res += str(n % 10)
            i += 1
            n //= 10
            if(i % 3 == 0 and n != 0):
                res += "."
            
        return res[::-1]