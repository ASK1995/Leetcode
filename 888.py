class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes))//2
        bobSizes = set(bobSizes)

        for candy in aliceSizes:
            if(candy - diff in bobSizes):
                return [candy, candy - diff]