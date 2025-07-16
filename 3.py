class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        letters = set()
        res = 0

        for i, letter in enumerate(s):
            letter = s[i]
            if(letter in letters):
                while(s[l] != letter):
                    letters.discard(s[l])
                    l += 1
                letters.discard(s[l])
                l += 1
            letters.add(letter)
            res = max(res, i - l + 1)
        return res