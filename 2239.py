class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]

        for num in nums:
            if(abs(res) > abs(num)):
                res = num
            elif(abs(res) == abs(num)):
                res = max(res, num)
        return res