from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        odd = False

        for value in count.values():
            res += value
            if(value % 2 != 0):
                res -= 1
                odd = True

        if(odd):
            res += 1

        return res