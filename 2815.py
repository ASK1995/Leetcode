class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = -1
        for i, num in enumerate(nums):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                digit1 = max(str(num1))
                digit2 = max(str(num2))
                if(digit1 == digit2):
                    res = max(res, num1 + num2)
        return res