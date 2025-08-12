class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob1(nums[1:]), self.rob1(nums[:-1]))

    def rob1(self, nums):
        max1, max2 = 0, 0

        for num in nums:
            max1, max2 = max2, max(max1 + num, max2)

        return max2