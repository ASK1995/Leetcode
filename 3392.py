class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l = 0
        res = 0
        while(l < len(nums) - 2):
            a, b, c = nums[l], nums[l + 1], nums[l + 2]
            if((a + c) == b/2):
                res += 1
            l += 1
        return res