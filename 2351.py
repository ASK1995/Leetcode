class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = set()
        for letter in s:
            if(letter in letters):
                return letter
            letters.add(letter)