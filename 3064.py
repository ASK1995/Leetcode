# Definition of commonSetBits API.
# def commonSetBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:
        res = 0

        for i in range(32):
            mask = 1 << i
            if(commonSetBits(mask)):
                res += mask
        return res