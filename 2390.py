class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        for letter in s:
            if(letter == '*'):
                l.pop()
            else:
                l.append(letter)
        return "".join(l)