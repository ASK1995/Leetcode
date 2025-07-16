from collections import defaultdict
from heapq import nlargest

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(lambda:[])
        for student, score in items:
            scores[student].append(score)
        keys = sorted(scores.keys())
        res = []
        for key in keys:
            vals = nlargest(5, scores[key])
            res.append([key, sum(vals)//5])
        return res