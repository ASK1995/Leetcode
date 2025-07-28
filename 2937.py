class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        l = 0

        while(l < len(s1) and l < len(s2) and l < len(s3)):
            if(s1[l] == s2[l] == s3[l]):
                l = l + 1
            else:
                break
        
        if(l == 0):
            return -1
        else:
            return len(s1) + len(s2) + len(s3) - 3*l