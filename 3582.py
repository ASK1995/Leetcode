class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        res = ""
        if(len(words) == 0):
            return "#"

        for index, word in enumerate(words):
            if(index == 0):
                res += '#' + word.lower()
            else:
                res += word.title()

        return res[:100]