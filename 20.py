class Solution:
    def isValid(self, s: str) -> bool:
        letters = []
        parentheses = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for letter in s:
            if letter in parentheses:
                if(len(letters) == 0):
                    return False
                if parentheses[letter] != letters[-1]:
                    return False
                else:
                    letters.pop()
            else:
                letters.append(letter)
        if len(letters) == 0:
            return True
        else:
            return False