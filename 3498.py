class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0

        for index, letter in enumerate(s):
            degree = 26 - (ord(letter) - ord('a'))
            res += degree * (index + 1)

        return res