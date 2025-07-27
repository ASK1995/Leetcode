from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = defaultdict(lambda:0)
        res = 0

        for num in nums:
            count[num] += 1
        
        for key, value in count.items():
            if value == 1:
                res += key

        return res