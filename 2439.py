class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        total = nums[0]

        for index in range(1, len(nums)):
            total += nums[index]
            res = max(res, math.ceil(total/(index + 1)))

        return res