class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []

        for letter in s:
            if(len(res) == 0):
                res.append(letter)
            elif(res[-1] == letter):
                res.pop()
            else:
                res.append(letter)

        return "".join(res)