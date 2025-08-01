from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        target = Counter("balloon")
        res = float('inf')

        for key, value in target.items():
            res = min(res, count[key]//target[key])
        return res