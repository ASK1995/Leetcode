class Solution:
    def isGood(self, nums: List[int]) -> bool:
        count = set()
        for num in nums:
            if num >= len(nums):
                return False
            if num in count:
                if num != len(nums) - 1:
                    return False
            count.add(num)

        return len(count) == len(nums) - 1