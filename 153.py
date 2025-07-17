class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = -1

        while(l <= r):
            m = (l + r)//2
            if(nums[m] > nums[-1]):
                l = m + 1
            else:
                res = m
                r = m - 1
        return nums[res]