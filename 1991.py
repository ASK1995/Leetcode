class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0

        for index, num in enumerate(nums):
            if(curr * 2 == total - num):
                return index

            curr += num

        return -1