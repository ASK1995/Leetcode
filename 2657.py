from collections import Counter

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count = Counter()
        res = []

        for a, b in zip(A, B):
            count[a] += 1
            count[b] += 1
            common = sum(1 for val in count.values() if val % 2 == 0)
            res.append(common)
        return res