class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        current = 'a'
        for letter in word:
            dist = abs(ord(letter) - ord(current))
            res = res + 1 + min(dist, 26 - dist)
            current = letter

        return res