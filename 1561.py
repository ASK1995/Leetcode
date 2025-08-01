class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        r = len(piles) - 2

        while(r >= len(piles)//3):
            res += piles[r]
            r -= 2

        return res