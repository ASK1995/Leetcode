class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')

        for i, num in enumerate(nums):
            total = 0
            while(num != 0):
                total += num % 10
                num //= 10

            res = min(res, total)

        return res