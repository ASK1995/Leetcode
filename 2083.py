from collections import Counter

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = Counter(s)
        res = 0

        for key, value in count.items():
            res += (value * (value + 1))//2

        return res