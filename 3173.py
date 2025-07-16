class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        res = []
        for index, num in enumerate(nums):
            if(index == len(nums) - 1):
                continue
            res.append(num | (nums[index + 1]))
        return res