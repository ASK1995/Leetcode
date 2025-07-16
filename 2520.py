class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        curr = num

        while(curr != 0):
            digit = curr % 10
            if(digit != 0):
                if(num % digit == 0):
                    res += 1
            curr //= 10
    
        return res