from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        count = sorted(count.values(), key = lambda x: x, reverse=True)
        res = 0
        curr = 0
        target = len(arr)//2
        for value in count:
            curr += value
            res += 1
            if(curr >= target):
                return res