class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set()
        res = 0

        for letter in word:
            s.add(letter)
        
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if(letter in s and letter.upper() in s):
                res += 1
        return res