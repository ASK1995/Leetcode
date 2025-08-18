class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total, max_average = 0, float('-inf')
        left = 0
        for index, num in enumerate(nums):
            total += num
            if(index - left + 1 == k):
                max_average = max(max_average, total/k)
                total -= nums[left]
                left += 1
        return max_average