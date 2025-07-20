class Solution:
    def isDecomposable(self, s: str) -> bool:
        l, r = 0, 1
        twos = 0
        while(r < len(s)):
            if(s[r] != s[l]):
                length = r - l
                if(length % 3 == 2):
                    twos += 1
                elif(length % 3 != 0):
                    return False
                l = r
            r += 1
        length = r - l
        if(length % 3 == 2):
            twos += 1
        elif(length % 3 != 0):
            return False
        return twos == 1