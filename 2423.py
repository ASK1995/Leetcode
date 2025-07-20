from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        for key in count.keys():
            count[key] -= 1
            s = set(value for value in count.values() if value != 0)
            if(len(s) == 1):
                return True
            count[key] += 1
        return False