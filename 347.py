from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda : 0)
        for num in nums:
            count[num] += 1
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