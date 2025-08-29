class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        left, right = -1, -1
        while(l <= r):
            m = l + (r - l)//2
            if(nums[m] < target):
                l = m + 1 
            else:
                r = m - 1
            if(nums[m] == target):
                left = m
        l, r = 0, len(nums) - 1
        while(l <= r):
            m = l + (r - l)//2
            if(nums[m] > target):
                r = m - 1 
            else:
                l = m + 1
            if(nums[m] == target):
                right = m
        if(left == -1):
            return False
        if((right - left + 1) > len(nums)//2):
            return True
        return False