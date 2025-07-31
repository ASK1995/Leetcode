from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)

        return (all(value == count[s[0]] for value in count.values()))