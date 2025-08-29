class Solution:
    def rob(self, nums: List[int]) -> int:
        max1, max2 = 0, 0

        for num in nums:
            max1, max2 = max(max2 + num, max1), max1

        return max1