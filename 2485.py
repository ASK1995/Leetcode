class Solution:
    def pivotInteger(self, n: int) -> int:
            total = (n *(n + 1))//2
            target = 0

            for i in range(1, n + 1):
                target += i
                if(target == (total - target + i)):
                    return i
                
            return -1