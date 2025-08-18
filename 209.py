class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        minimum = float('inf')

        for index, num in enumerate(nums):
            total += num
            while(total >= target):
                minimum = min(minimum, index - left + 1)
                total -= nums[left]
                left += 1

        return minimum if minimum != float('inf') else 0