class Solution:
    def greatestLetter(self, s: str) -> str:
        max_letter = -1
        x = set()
        for letter in s:
            x.add(letter)
            if(letter.lower() in x and letter.upper() in x):
                max_letter = max(max_letter, ord(letter.upper()))
        if(max_letter == -1):
            return ""
        return chr(max_letter)