class Solution:
    def rob(self, nums: List[int]) -> int:
        max1, max2 = 0, 0

        for num in nums:
            max1, max2 = max2, max(max1 + num, max2)

        return max2