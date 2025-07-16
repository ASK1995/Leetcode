from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1 = defaultdict(lambda : 0)
        res = 0
        for letter in s:
            count1[letter] += 1
        for letter in t:
            if(count1[letter] >= 1):
                count1[letter] -= 1
            else:
                res += 1
        return res