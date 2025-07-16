class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for index, num in enumerate(nums):
            if(index > reachable):
                return False
            reachable = max(reachable, index + num)

        return reachable >= len(nums) - 1