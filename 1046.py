import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)
        while(len(stones) > 1):
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if(x != y):
                x -= y
                heapq.heappush(stones, x)
        if stones:
            return stones[0] * -1
        return 0