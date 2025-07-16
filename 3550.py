class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            res = 0
            while(num != 0):
                res += num % 10
                num //= 10
            if(res == index):
                return index
        return -1