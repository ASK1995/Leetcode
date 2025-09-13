import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        s = set([1])
        for i in range(n - 1):
            val = heapq.heappop(res)
            for mul in [2, 3, 5]:
                num = val * mul
                if num not in s:
                    heapq.heappush(res, num)
                    s.add(num)

        return res[0] 