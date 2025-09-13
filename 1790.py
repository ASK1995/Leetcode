class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = []
        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                c.append(i)
        if(len(c) == 2):
            if s1[c[0]] == s2[c[1]] and s1[c[1]] == s2[c[0]]:
                return True
            return False
        return not c