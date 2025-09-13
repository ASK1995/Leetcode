from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        letters = Counter()
        target = Counter(p)
        left = 0
        res = []

        for index, letter in enumerate(s):
            letters[letter] += 1
            if(len(p) == index - left + 1):
                if(letters == target):
                    res.append(left)
                letters[s[left]] -= 1
                if(letters[s[left]] == 0):
                    del letters[s[left]]
                left += 1

        return res