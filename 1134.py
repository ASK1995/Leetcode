class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        check = n
        while(n != 0):
            digit = n % 10
            n //= 10
            check -= (digit ** k)
        return check == 0