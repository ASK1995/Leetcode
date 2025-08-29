from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = Counter(s)

        counts = sorted(count.values())
        return sum(counts[:-k])