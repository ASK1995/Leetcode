class Solution:
    def secondHighest(self, s: str) -> int:
        highest, second = -1, -1

        for letter in s:
            if(letter.isnumeric()):
                val = int(letter)
                if(val > highest):
                    highest, second = val, highest
                elif(val != highest and val > second):
                    second = val
        return second