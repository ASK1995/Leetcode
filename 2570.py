from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        count = defaultdict(lambda:0)
        res = []

        for index, val in nums1:
            count[index] += val
        for index, val in nums2:
            count[index] += val
        counts = sorted(count.items())
        for count in counts:
            res.append(count)
        return res