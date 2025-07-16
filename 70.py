class Solution:
    def climbStairs(self, n: int) -> int:
        if(n <= 3):
            return n
        curr, prev = 3, 2
        for i in range(4, n + 1):
            curr, prev = curr + prev, curr
        return curr