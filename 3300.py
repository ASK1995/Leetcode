class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            res = 0
            while(num != 0):
                res += num % 10
                num //= 10
            nums[i] = res

        return min(nums)