import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit = []
        min_capital = [(cap, profit) for cap, profit in zip(capital, profits)]
        heapq.heapify(min_capital)

        for i in range(k):
            while min_capital and min_capital[0][0] <= w:
                c, p = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -1 * p)
            if max_profit:
                w += heapq.heappop(max_profit) * -1
            else:
                break

        return w