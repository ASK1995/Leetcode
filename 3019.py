class Solution:
    def countKeyChanges(self, s: str) -> int:
        res, prev = 0, None

        for letter in s:
            if(prev != None and prev != letter.lower()):
                res += 1
            prev = letter.lower()
        return res