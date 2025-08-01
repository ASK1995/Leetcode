class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = float('-inf')
        
        for i, value in enumerate(number):
            if(value == digit):
                res = max(int(number[:i] + number[i+1:]), res)
        
        return str(res)