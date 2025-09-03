class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        prev = nums[0] - 1

        for num in nums:
            if num <= prev:
                new_num = prev + 1
                res += (new_num - num)
                prev = new_num
            else:
                prev = num

        return res