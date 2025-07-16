class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = [0] + flowerbed + [0]
        res = 0

        for i in range(1, len(l) - 1):
            if(l[i - 1] == 0 and l[i] == 0 and l[i + 1] == 0):
                l[i] = 1
                res += 1
        return res >= n