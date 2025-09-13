class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(total):
            current = 0
            parts = 1
            for num in nums:
                if current + num > total:
                    current = num
                    parts += 1
                else:
                    current += num
            return parts <= k

        l, r = max(nums), sum(nums)
        res = sum(nums)

        while(l <= r):
            m = (l + r)//2
            if(canSplit(m)):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
