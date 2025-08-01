class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        s = set(brokenLetters)
        words = text.split()

        for word in words:
            letters = set(word)
            if(len(letters.intersection(s)) == 0):
                count += 1

        return count