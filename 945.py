class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        prev = nums[0]

        for index in range(1, len(nums)):
            diff = nums[index - 1] + 1 - nums[index]
            if(nums[index] <= prev):
                res += diff
                nums[index] += diff
            prev = nums[index]

        return res