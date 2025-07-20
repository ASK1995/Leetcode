from heapq import nlargest

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        top3 = nlargest(3, nums)
        low2 = nlargest(2, nums, key = lambda x : -x)

        return max(top3[0] * low2[0] * low2[1], top3[0] * top3[1] * top3[2])