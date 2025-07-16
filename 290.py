from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if(len(pattern) != len(s)):
            return False
        char_to_word = defaultdict(lambda:0)
        word_to_char = defaultdict(lambda:0)
        
        for c, w in zip(pattern, s):
            if(char_to_word[c] != 0 and char_to_word[c] != w):
                return False
            if(word_to_char[w] != 0 and word_to_char[w] != c):
                return False
            char_to_word[c] = w
            word_to_char[w] = c
        return True