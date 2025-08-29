class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        for index in range(len(nums) - 1):
            if(nums[index] == nums[index + 1]):
                nums[index + 1] = 0
                if(nums[index] != 0):
                    res.append(nums[index] * 2)
            elif(nums[index] != 0):
                res.append(nums[index])
        res.append(nums[-1])
        while(len(res) < len(nums)):
            res.append(0)
        return res