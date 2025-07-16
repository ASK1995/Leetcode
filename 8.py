class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        neg = False
        res = 0
        for index, letter in enumerate(s):
            if(index == 0):
                if(s[index] == '-'):
                    neg = True
                    continue
                elif(s[index] == '+'):
                    continue
            if(letter.isnumeric()):
                res = res * 10 + int(letter)
            else:
                break
        if(neg):
            res *= -1
        if(res > 2**31 - 1):
            res = 2 ** 31 - 1
        elif(res < -2 ** 31):
            res = -2 ** 31
        return res