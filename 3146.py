from collections import defaultdict

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        mapper = defaultdict(lambda : 0)
        res = 0

        for index, letter in enumerate(s):
            mapper[letter] = index

        for index, letter in enumerate(t):
            res += abs(index - mapper[letter])
        
        return res