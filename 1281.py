class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, total = 1, 0
        while(n != 0):
            digit = n % 10
            prod = prod * digit
            total += digit
            n //= 10
        return prod - total