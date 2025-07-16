from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pair = defaultdict(lambda:0)
        for i, j in dominoes:
            i, j = min(i, j), max(i, j)
            pair[(i, j)] += 1
        res = 0
        for key, value in pair.items():
            if(value != 1):
                res += (value) * (value - 1)//2
        return res