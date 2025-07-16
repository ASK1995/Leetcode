from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        count = Counter(s)

        for letter in t:
            count[letter] -= 1
            if(count[letter] < 0):
                return False
        
        return True