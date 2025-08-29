class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        res = 0
        while(l <= r):
            m = (l + r)//2
            if(m * (m + 1)//2 <= n):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res