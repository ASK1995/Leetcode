from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_count = max(count.values())
        start, end = {}, {}
        min_len = float('inf')
        for index, num in enumerate(nums):
            if num not in start:
                start[num] = index
            else:
                end[num] = index
            max_count = max(max_count, count[num])

        for key, value in count.items():
            if(value == max_count):
                if(value == 1):
                    return 1
                min_len = min(min_len, end[key] - start[key] + 1)

        return min_len