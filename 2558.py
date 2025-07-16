import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-1 * gift for gift in gifts]
        res = 0
        heapq.heapify(gifts)

        while(k != 0):
            x = heapq.heappop(gifts)
            heapq.heappush(gifts, -1 * math.floor(math.sqrt(x * -1)))
            k -= 1

        return sum(gifts) * -1