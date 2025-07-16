from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd, min_even = 0, float('inf')
        count = Counter(s)

        for value in count.values():
            if(value % 2 != 0):
                max_odd = max(max_odd, value)

            if(value % 2 == 0):
                min_even = min(value, min_even)

        return max_odd - min_even