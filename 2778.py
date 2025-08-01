class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for index, num in enumerate(nums):
            if(n % (index + 1) == 0):
                res += num**2

        return res