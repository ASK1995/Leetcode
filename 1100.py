from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        res = 0
        left = 0
        letters = Counter()

        for i, letter in enumerate(s):
            letters[letter] += 1
            if(i - left + 1 == k):
                if(len(letters) == k):
                    res += 1
                letters[s[left]] -= 1
                if(letters[s[left]] == 0):
                    del letters[s[left]]
                left += 1

        return res