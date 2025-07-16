from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = Counter(s)
        count = sorted(count.values())

        return sum(count[:-k])