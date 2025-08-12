from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(lambda : 0)
        for num in arr:
            count[num] += 1
        counts = set(count.values())
        if(len(count) == len(counts)):
            return True
        return False