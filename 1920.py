class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for index, value in enumerate(nums):
            ans.append(nums[nums[index]])
        return ans