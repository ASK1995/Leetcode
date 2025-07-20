class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        res = ""
        for index, letter in enumerate(s):
            res += letter
            n = len(res)
            k = len(s)
            if(k % n == 0 and index != k - 1):
                mul = k // n
                if((res * mul) == s):
                    return True
        return False