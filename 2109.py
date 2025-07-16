class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        i = 0
        for index, letter in enumerate(s):
            if(i < len(spaces) and index == spaces[i]):
                res += " "
                i += 1
            res += s[index]

        return res