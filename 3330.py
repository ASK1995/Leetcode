class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        prev = None

        for letter in word:
            if(prev == letter):
                res += 1
            prev = letter

        return res