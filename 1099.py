class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = -1
        while(l < r):
            total = nums[l] + nums[r]
            if(total >= k):
                r -= 1
            else:
                res = max(res, total)
                l += 1
        return res