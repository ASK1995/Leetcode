from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
      
        sorted_count = sorted(nums, key=lambda x: (count[x], -x))
      
        return sorted_count