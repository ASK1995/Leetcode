class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        left = 0

        for index, num in enumerate(nums):
            if(num <= 0):
                left = index
        right = left + 1
        while(left < right and left >= 0 and right < n):
            l, r = nums[left]**2, nums[right]**2
            if(l <= r):
                res.append(l)
                left -= 1
            else:
                res.append(r)
                right += 1

        while(left >= 0):
            l = nums[left]**2
            res.append(l)
            left -= 1

        while(right < n):
            r = nums[right]**2
            res.append(r)
            right += 1

        return res