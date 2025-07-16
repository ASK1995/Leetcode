class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        low = min(nums)
        s = set([num for num in range(low, low + len(nums))])

        for num in nums:
            if num in s:
                s.discard(num)
            else:
                return False

        return True