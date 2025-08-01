class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            val = str(num)
            res += int(max(val)*len(val))

        return res