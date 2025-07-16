class Solution:
    def clearDigits(self, s: str) -> str:
        l = []

        for letter in s:
            if(letter.isalpha()):
                l.append(letter)
            elif(letter.isnumeric()):
                if(len(l) != 0):
                    l.pop()
        
        return "".join(l)