class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        i = 0
        while(i < len(s)):
            res += s[i]
            if(i + 1 < len(s)):
                res += chr(ord(s[i]) + int(s[i + 1]))
            i += 2
        return res