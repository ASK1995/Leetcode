class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while(l <= r):
            m = (l + r)//2
            current = 0
            for pile in piles:
                if(pile % m == 0):
                    current += pile//m
                else:
                    current += pile//m + 1
            if(current <= h):
                r = m - 1
                res = m
            else:
                l = m + 1

        return res