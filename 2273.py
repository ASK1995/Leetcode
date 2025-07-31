from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        prev_count = Counter(words[0])
        res = [words[0]]

        for index, word in enumerate(words):
            if(index == 0):
                continue
            count = Counter(word)
            if(count != prev_count):
                res.append(word)
            prev_count = count

        return res