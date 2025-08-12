class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total, left = 0, 0
        res = float('-inf')

        for index, num in enumerate(nums):
            total += num
            if(index - left + 1 == k):
                res = max(res, total/k)
                total -= nums[left]
                left += 1
        return res