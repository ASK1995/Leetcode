class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = False
        for num in nums:
            if num < 0:
                neg = not neg
            elif num == 0:
                return 0
        
        if(neg):
            return -1
        return 1