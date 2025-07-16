from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter()
        check = Counter(p)
        l = 0
        res = []

        for index, letter in enumerate(s):
            count[letter] += 1
            if(index - l + 1 == len(p)):
                if(count == check):
                    res.append(l)
                count[s[l]] -= 1
                if(count[s[l]] == 0):
                    del count[s[l]]
                l += 1
        return res