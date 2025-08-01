class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = 0
        val = max(nums)

        while k != 0:
            k -= 1
            res += val
            val += 1

        return res