class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.split('-'))
        l, r = 0, len(s) - 1
        res = ""

        while(r >= 0):
            res += s[r].upper()
            l += 1
            if((l % k == 0) and (r != 0)):
                res += '-'
            r -= 1
        return res[::-1]