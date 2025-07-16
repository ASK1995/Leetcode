class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        vals = []
        res = ""
        for letter in s:
            if(letter.lower() in vowels):
                vals.append(ord(letter))
        vals.sort()
        i = 0
        for index, letter in enumerate(s):
            if(letter.lower() not in vowels):
                res += letter
            else:
                res += chr(vals[i])
                i += 1
        return res