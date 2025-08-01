from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count = Counter(s)
        min_copies = float('inf')

        target_count = Counter(target)

        for key, value in target_count.items():
            min_copies = min(min_copies, count[key] // target_count[key])

        return min_copies