class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd = 0

        for num in nums:
            if(num % 2 != 0):
                odd += 1

        return [0]*(len(nums) - odd) + [1]*odd