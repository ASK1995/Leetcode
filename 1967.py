class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0

        for pattern in patterns:
            if(word.find(pattern) != -1):
                res += 1

        return res