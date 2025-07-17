class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        lowest = float('inf')
        for i in range(len(nums) - k + 1):
            lowest = min(lowest, nums[i] - nums[k - 1 + i])
        return lowest