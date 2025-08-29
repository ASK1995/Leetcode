class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = ""
        l = 0

        while(l < len(s)):
            total = 0
            for i in range(k):
                total += ord(s[l + i]) - ord('a')
            total = total % 26
            res += chr(ord('a') + total)
            l += k

        return res