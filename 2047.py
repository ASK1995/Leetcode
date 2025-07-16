class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        res = 0

        for word in words:
            valid = True
            hyphen, punctutation = 0, 0
            for index, letter in enumerate(word):
                if(letter.isnumeric()):
                    valid = False
                elif(letter == '-'):
                    hyphen += 1
                    if(hyphen > 1):
                        valid = False
                    if(index - 1 >= 0 and index + 1 < len(word)):
                        prev, newer = word[index - 1], word[index + 1]
                        if(not (prev.isalpha() and newer.isalpha())):
                            valid = False
                    else:
                        valid = False
                elif(letter in ['!', '.', ',', ' ']):
                    punctutation += 1
                    if(punctutation <= 1):
                        if(index != len(word) - 1):
                            valid = False
                    else:
                        valid = False
            if(valid):
                res += 1
        return res