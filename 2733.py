class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)

        for num in nums:
            if(num != min_num and max_num != num):
                return num

        return -1