from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        vowel_max, consonant_max = 0, 0
        letters = Counter(s)

        for key, value in letters.items():
            if(key in vowels):
                vowel_max = max(vowel_max, value)
            else:
                consonant_max = max(consonant_max, value)

        return vowel_max + consonant_max