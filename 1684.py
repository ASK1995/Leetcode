class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        check = set(allowed)
        for word in words:
            if(all(letter in check for letter in word)):
                res += 1
        return res