class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, res = 0, 0
        zeroes = 0

        for index, num in enumerate(nums):
            if(num == 0):
                zeroes += 1
            while(zeroes > 1):
                if(nums[l] == 0):
                    zeroes -= 1
                l += 1
            res = max(res, index - l + 1 - zeroes)

        return res if res != len(nums) else res - 1