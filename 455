class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i1, i2 = 0, 0
        count = 0

        while(i1 < len(g) and i2 < len(s)):
            if(g[i1] <= s[i2]):
                count += 1
                i1 += 1
                i2 += 1
            else:
                i2 += 1
            
        return count