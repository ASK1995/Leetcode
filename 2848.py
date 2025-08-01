class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key = lambda x: x[0])
        start, end = nums[0][0], nums[0][1]
        res = 0

        for num in nums:
            if(num[0] <= end):
                end = max(end, num[1])
            else:
                res += end - start + 1
                start, end = num[0], num[1]

        return res + end - start + 1