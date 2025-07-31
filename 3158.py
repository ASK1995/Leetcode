class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s = set()
        res = 0

        for num in nums:
            if(num in s):
                res ^= num
            else:
                s.add(num)

        return res