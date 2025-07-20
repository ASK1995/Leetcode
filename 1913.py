class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        largest_prod = nums[-1] * nums[-2]
        smallest_prod = nums[0] * nums[1]
        return largest_prod - smallest_prod