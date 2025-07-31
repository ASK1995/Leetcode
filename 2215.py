class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        nums1, nums2 = nums1 - nums2, nums2 - nums1
        ans = [list(nums1), list(nums2)]

        return ans