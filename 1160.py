from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        letters = Counter(chars)
        res = 0

        for word in words:
            count = Counter(word)
            if(all(letters[key] >= count[key] for key in count.keys())):
                res += len(word)

        return res