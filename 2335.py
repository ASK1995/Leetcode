import heapq

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        amount = [-x for x in amount if x != 0]
        heapq.heapify(amount)

        while(amount):
            x = heapq.heappop(amount)
            if(len(amount) == 0):
                return res + x * -1
            y = heapq.heappop(amount)
            res += 1
            y += 1
            x += 1
            if(y < 0):
                heapq.heappush(amount, y)
            if(x < 0):
                heapq.heappush(amount, x)
        return res