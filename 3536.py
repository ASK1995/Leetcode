class Solution:
    def maxProduct(self, n: int) -> int:
        digit1, digit2 = 0, 0

        while(n != 0):
            current = n % 10
            if(current > digit1):
                digit1, digit2 = current, digit1
            elif(current > digit2):
                digit2 = current
            n //= 10

        return digit1 * digit2