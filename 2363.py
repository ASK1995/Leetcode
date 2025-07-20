from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count = defaultdict(lambda:0)
        for key, value in items1:
            count[key] += value
        for key, value in items2:
            count[key] += value
        count = dict(sorted(count.items(), key = lambda x: x[0]))
        return list(count.items())