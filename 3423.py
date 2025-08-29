class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0

        for index, num in enumerate(nums):
            res = max(res, abs(num - nums[(index + 1) % len(nums)]))

        return res