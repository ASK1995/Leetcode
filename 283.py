class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for index, value in enumerate(nums):
            if(value != 0):
                nums[i] = value
                i += 1

        for index in range(i, len(nums)):
            nums[index] = 0