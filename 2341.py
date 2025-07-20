class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        s = set()
        res = 0
        for num in nums:
            if(num in s):
                s.discard(num)
                res += 1
            else:
                s.add(num)
        return [res, len(s)]