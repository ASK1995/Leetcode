from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(lambda : 0)
        for num in arr:
            count[num] += 1
        counts = set()
        for key, value in count.items():
            if(value in counts):
                return False
            counts.add(value)
        return True