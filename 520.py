class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up = 0
        for letter in word:
            if(letter.isupper()):
                up += 1
        return (up == 0 or up == len(word)) or (up == 1 and word[0].isupper())