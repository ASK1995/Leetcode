class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res, current = 0, 0
        for letter in s:
            if(letter == 'L'):
                current -= 1
            else:
                current += 1
            if(current == 0):
                res += 1
        return res