class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1

        while(l < r):
            while(l < len(s) and not s[l].isalpha()):
                l += 1

            while(r >= 0 and not s[r].isalpha()):
                r -= 1

            if(l < len(s) and r >= 0 and l < r):
                s[l], s[r] = s[r], s[l]

            l, r = l + 1, r - 1

        return "".join(s)