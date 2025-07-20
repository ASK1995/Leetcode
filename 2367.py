class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)

        res = sum(x + diff in s and x + 2 * diff in s for x in nums)

        return res