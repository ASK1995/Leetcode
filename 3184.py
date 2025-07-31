from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        duration = defaultdict(lambda:[])
        pairs = 0
        for hour in hours:
            check = hour % 24
            pairs += len(duration[(24 - check) % 24])
            duration[check].append(check)
        return pairs