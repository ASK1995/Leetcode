class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for index1 in range(len(nums)):
            for index2 in range(index1 + 1, len(nums)):
                if(abs(nums[index2] - nums[index1]) == k):
                    count += 1
        
        return count