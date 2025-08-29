class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s) != 2):
            l = []

            for i in range(len(s) - 1):
                l.append((int(s[i]) + int(s[i + 1])) % 10)

            s = l

        return s[0] == s[1]