class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            total = 0
            while(num != 0):
                total += num % 10
                num //= 10
            if(total == index):
                return index

        return -1