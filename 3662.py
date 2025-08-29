from collections import Counter

class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        count = Counter(s)
        res = ""

        for index, letter in enumerate(s):
            if(count[letter] < k):
                res += letter

        return res