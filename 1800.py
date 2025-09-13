class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total, max_sum = nums[0], nums[0]
        prev = nums[0]

        for index in range(1, len(nums)):
            if(nums[index] <= prev):
                total = nums[index]
            else:
                total += nums[index]
            prev = nums[index]
            max_sum = max(total, max_sum)

        return max_sum