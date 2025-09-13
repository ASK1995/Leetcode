class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        max_till_now = nums[0]
        max_diff = 0

        for k in range(1, len(nums)):
            res = max(res, max_diff * nums[k])
            max_till_now = max(max_till_now, nums[k])
            max_diff = max(max_diff, max_till_now - nums[k])

        return res