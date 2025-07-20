class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l_res, r_res = -1, -1
        l, r = 0, len(nums) - 1
        while(l <= r):
            m = (l + r)//2
            if(nums[m] == target):
                l_res = m
                r = m - 1
            elif(nums[m] > target):
                r = m - 1
            else:
                l = m + 1
        l, r = 0, len(nums) - 1
        while(l <= r):
            m = (l + r)//2
            if(nums[m] == target):
                r_res = m
                l = m + 1
            elif(nums[m] > target):
                r = m - 1
            else:
                l = m + 1
        return [l_res, r_res]