from collections import defaultdict

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        index = defaultdict(lambda:0)
        res = 0
        prev = 0

        for i, letter in enumerate(keyboard):
            index[letter] = i


        for letter in word:
            res += abs(index[letter] - prev)
            prev = index[letter]

        return res