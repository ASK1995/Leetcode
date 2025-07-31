class Solution:
    def isThree(self, n: int) -> bool:
        s = set()
        i = 2

        while(i * i < n):
            if(n % i == 0):
                return False
            i += 1
        return i * i == n