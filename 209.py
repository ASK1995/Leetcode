class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, total = 0, 0
        min_size = float('inf')
        for index, num in enumerate(nums):
            total += num
            if(total >= target):
                while(start <= index) and (total - nums[start] >= target):
                    total -= nums[start]
                    start += 1
                min_size = min(min_size, index - start + 1)
        return min_size if min_size != float('inf') else 0