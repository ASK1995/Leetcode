class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for index, value in enumerate(nums):
            res ^= (index + 1) ^ value
        return res