class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        l = [""]*len(s)

        for i in range(len(s)):
            l[int(s[i][-1]) - 1] = s[i][:-1]

        return " ".join(l)