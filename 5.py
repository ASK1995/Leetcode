class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        length = 0

        def check(l, r):
            nonlocal length, start, end
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if(r - l + 1 > length):
                    length = r - l + 1
                    start, end = l, r + 1
                l, r = l - 1, r + 1
                

        for i in range(len(s)):
            check(i, i)
            check(i, i + 1)

        return s[start:end]