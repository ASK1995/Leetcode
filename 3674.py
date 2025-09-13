class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if(all(num == nums[0] for num in nums)):
            return 0
        return 1