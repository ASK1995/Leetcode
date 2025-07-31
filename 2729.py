class Solution:
    def isFascinating(self, n: int) -> bool:
        s = set()
        val = str(n) + str(n*2) + str(n*3)

        for letter in val:
            if(letter in s):
                return False
            s.add(letter)

        return (len(s) == 9) and ('0' not in s)