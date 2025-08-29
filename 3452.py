class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0

        for index, num in enumerate(nums):
            if(index - k >= 0):
                if(num <= nums[index - k]):
                    continue
            if(index + k < len(nums)):
                if(num <= nums[index + k]):
                    continue

            res += num

        return res