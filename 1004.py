class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, res = 0, 0
        zeroes = 0

        for index, num in enumerate(nums):
            if(num == 0):
                zeroes += 1
            while(zeroes > k):
                if(nums[l] == 0):
                    zeroes -= 1
                l += 1
            res = max(res, index - l + 1)
        return res