class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        res = max(0, (n - k)*k) + max(0, (m - k)*k)
        return res