from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = defaultdict(lambda : 0)
        max_count = 0

        for num in nums:
            count[num] += 1
            max_count = max(max_count, count[num])

        res = 0
        for key, value in count.items():
            if(value == max_count):
                res += value

        return res