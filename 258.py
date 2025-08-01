class Solution:
    def addDigits(self, num: int) -> int:
        digit_sum = 0

        while(num != 0):
            digit_sum += (num % 10)
            num //= 10
            if(num == 0):
                if(digit_sum < 10):
                    return digit_sum
                else:
                    num = digit_sum
                    digit_sum = 0

        return 0