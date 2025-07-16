from collections import defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = defaultdict(lambda: 0)
        res = []
        for index, num in enumerate(nums2):
            mapping[num] = index
        for num in nums1:
            res.append(mapping[num])
        return res