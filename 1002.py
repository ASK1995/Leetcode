from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words:
            cur_count = Counter(word)
            for letter in count:
                count[letter] = min(count[letter], cur_count[letter])
        
        res = []
        for key in count:
            for val in range(count[key]):
                res.append(key)
        return res