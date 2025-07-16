class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        jewel = set(jewels)
        for stone in stones:
            if stone in jewel:
                res += 1
        return res