class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]

        while(len(nums) != 1):
            newnums = []
            for i in range(len(nums)//2):
                if(i % 2 == 0):
                    newnums.append(min(nums[2*i], nums[2*i + 1]))
                else:
                    newnums.append(max(nums[2*i], nums[2*i + 1]))

            nums = newnums

        return nums[0]