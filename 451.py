from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        s = sorted(s, key = lambda x: (count[x], x), reverse = True)
        return "".join(s)