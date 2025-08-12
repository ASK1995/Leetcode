class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')
        for i in range(len(nums)):
            num = nums[i]
            rev = 0
            while(num != 0):
                rev += num % 10
                num //= 10
            res = min(res, rev)

        return res