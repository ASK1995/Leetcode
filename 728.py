class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            x = i
            dividing = True
            while(x != 0):
                digit = x % 10
                x //= 10
                if((digit == 0) or ((i % digit) != 0)):
                    dividing = False
                    break
            if(dividing):
                res.append(i)
        return res