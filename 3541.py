from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        vowel_max, consonant_max = 0, 0
        letters = Counter(s)

        for key in letters.keys():
            value = letters[key]
            if(key in vowels):
                vowel_max = max(vowel_max, value)
            else:
                consonant_max = max(consonant_max, value)
        return vowel_max + consonant_max