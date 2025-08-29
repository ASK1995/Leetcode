class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        letters = set()
        left = 0
        res = 0

        for index, letter in enumerate(s):
            while(letter in letters):
                letters.discard(s[left])
                left += 1
            letters.add(letter)
            res += index - left + 1

        return res