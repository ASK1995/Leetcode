class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        for r in range(len(nums)):
            if(nums[r] != 0):
                nums[l] = nums[r]
                l += 1
        for l in range(l, len(nums)):
            nums[l] = 0