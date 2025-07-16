class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0] * (n + 1)

        for i in range(1, n + 1):
            count[i] = 1 + count[i & (i - 1)]
        
        return count