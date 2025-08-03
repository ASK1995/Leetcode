from collections import Counter
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        freq = []
        for key, value in count.items():
            heappush(freq, (value, key))
            if(len(freq) > k):
                heappop(freq)

        res = []
        for i in range(k):
            count, key = heappop(freq)
            res.append(key)

        return res