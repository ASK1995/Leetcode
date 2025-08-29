class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 1
        count = 0

        def check(l, r):
            nonlocal res, count
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if(r - l + 1 > res):
                    res = r - l + 1
                count += 1
                l -= 1
                r += 1

        for index, letter in enumerate(s):
            check(index, index)
            check(index, index + 1)

        return count