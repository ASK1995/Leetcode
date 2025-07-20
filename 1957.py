class Solution:
    def makeFancyString(self, s: str) -> str:
        l = []

        for letter in s:
            if(len(l) >= 2):
                if(letter == l[-2] == l[-1]):
                        continue
            l.append(letter)

        return "".join(l)