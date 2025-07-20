import math

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = a**2 + b**2
                root = int(math.sqrt(c))
                if(root <= n and root**2 == c):
                    res += 1
        return res