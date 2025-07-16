from collections import defaultdict

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = defaultdict(lambda:0), defaultdict(lambda:0)

        for num in nums1:
            count1[num] += 1
        for num in nums2:
            count2[num] += 1
        res1, res2 = 0, 0
        for num in nums1:
            if(count2[num] != 0):
                res1 += 1
        for num in nums2:
            if(count1[num] != 0):
                res2 += 1
        return [res1, res2]