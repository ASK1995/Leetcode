class Solution:
    def maxProduct(self, n: int) -> int:
        digit1, digit2 = 0, 0
        while(n != 0):
            digit = n % 10
            if(digit > digit1):
                digit1, digit2 = digit, digit1
            elif(digit > digit2):
                digit2 = digit
            n //= 10
        return digit1 * digit2