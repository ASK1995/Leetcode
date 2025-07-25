class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        
        while(numBottles > 0):
            res += numBottles
            empty += numBottles
            numBottles = empty//numExchange
            empty %= numExchange
        return res