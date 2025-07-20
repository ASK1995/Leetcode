from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        res = []
        for key, value in count1.items():
            min_count = min(value, count2[key])
            for i in range(min_count):
                res.append(key)
        return res 