class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        prev = None
        for i, num in enumerate(nums):
            if(num == prev):
                continue
            prev = num
            l, r = i + 1, len(nums) - 1
            while(l < r):
                total = num + nums[l] + nums[r]
                if(total == 0):
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while(nums[l] == nums[l - 1] and l < r):
                        l += 1
                elif(total > 0):
                    r -= 1
                else:
                    l += 1
        return res