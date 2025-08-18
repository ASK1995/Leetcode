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
                del_letter = s[left]
                letters[del_letter] -= 1
                left += 1
                if(letters[del_letter] == 0):
                    del letters[del_letter]

        return res