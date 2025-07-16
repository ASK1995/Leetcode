from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        res = -1
        count = defaultdict(lambda:0)
        for num in nums:
            count[num] += 1
        
        for key, value in count.items():
            if(value == 1):
                res = max(res, key)

        return res