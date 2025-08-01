from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(lambda:0)

        for num in nums:
            for val in num:
                count[val] += 1

        res = []
        for key, value in count.items():
            if(value == len(nums)):
                res.append(key)

        return sorted(res)