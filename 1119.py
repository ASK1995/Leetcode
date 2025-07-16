class Solution:
    def removeVowels(self, s: str) -> str:
        res = ""
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for letter in s:
            if letter not in vowels:
                res += letter
        return res