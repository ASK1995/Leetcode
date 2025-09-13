class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums) - 1):
            if(nums[index] == nums[index + 1]):
                nums[index] *= 2
                nums[index + 1] = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l] = nums[i]
                l += 1
        for l in range(l, len(nums)):
            nums[l] = 0
        return nums