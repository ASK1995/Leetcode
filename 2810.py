class Solution:
    def finalString(self, s: str) -> str:
        res = ""

        for letter in s:
            if(letter == 'i'):
                res = res[::-1]
            else:
                res += letter
        
        return res