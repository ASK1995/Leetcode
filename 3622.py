class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total, prod = 0, 1
        num = n
        while(n != 0):
            total += (n % 10)
            prod *= (n % 10)
            n //= 10

        if (total + prod == 0):
            return False

        return (num % (total + prod) == 0)