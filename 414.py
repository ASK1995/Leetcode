import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if(len(nums) < 3):
            return max(nums)
        heapq.heapify(nums)
        three = heapq.nlargest(3, nums)

        return three[-1]