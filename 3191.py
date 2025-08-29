class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = 0
        res = 0

        while(l < len(nums) - 2):
            if(nums[l] == 0):
                res += 1
                nums[l + 1] ^= 1
                nums[l + 2] ^= 1
            l += 1

        if(nums[-1] == 1 and nums[-2] == 1):
            return res
        return -1