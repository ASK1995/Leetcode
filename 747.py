class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x = max(nums)
        res = nums.index(x)

        for index, num in enumerate(nums):
            if(x != num and x < 2*num):
                return -1

        return res