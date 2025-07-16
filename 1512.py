from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for key in count.keys():
            value = count[key]
            res += (value * (value - 1))//2
        return res