class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        n = len(s)
        if(0 in nums):
            return n - 1
        return n