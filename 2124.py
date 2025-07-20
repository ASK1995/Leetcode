class Solution:
    def checkString(self, s: str) -> bool:
        first_b = False

        for letter in s:
            if(letter == 'b'):
                if(not first_b):
                    first_b = True
            elif(letter == 'a'):
                if(first_b):
                    return False

        return True