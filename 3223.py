from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        res = 0

        for key, value in count.items():
            while(value > 2):
                value -= 2
            res += value

        return res