class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        res = set()
        max_ans = 0

        for num in nums:
            if((num * -1) in s):
                res.add(abs(num))
                max_ans = max(max_ans, abs(num))
            s.add(num)
        if max_ans == 0:
            return -1
        else:
            return max_ans