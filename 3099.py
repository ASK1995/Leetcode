class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = 0
        n = x

        while(n != 0):
            total += n % 10
            n //= 10

        if(x % total == 0):
            return total
        return -1