class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        text = text.split()

        if(len(text) == 1):
            return "".join(text) + spaces * " "
        gaps = spaces // (len(text) - 1)
        extra = spaces % (len(text) - 1)
        sep = " " * gaps

        return sep.join(text) + " " * extra