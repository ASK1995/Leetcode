class Solution:
    def generateTag(self, caption: str) -> str:
        res = "#"
        captions = caption.split()
        if(len(captions) == 0):
            return res

        res += captions[0].lower()
        for i in range(1, len(captions)):
            res += captions[i].title()

        return res[:100]