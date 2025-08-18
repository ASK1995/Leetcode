class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, val in enumerate(nums):
            if(i > 0 and nums[i - 1] == nums[i]):
                continue
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                total = val + nums[j] + nums[k]
                if(total == 0):
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while(j < k and nums[j] == nums[j - 1]):
                        j += 1
                    k -= 1
                elif(total < 0):
                    j += 1
                else:
                    k -= 1

        return res