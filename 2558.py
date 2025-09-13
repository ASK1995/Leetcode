import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        
        while(k != 0):
            gift = heapq.heappop(gifts)
            heapq.heappush(gifts, -1 *math.floor(math.sqrt(-gift)))
            k -= 1

        return sum(gifts) * -1