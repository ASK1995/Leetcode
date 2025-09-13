class Solution:
    def partitionString(self, s: str) -> int:
        letters = set()
        k = 1

        for index in range(len(s)):
            if s[index] in letters:
                k += 1
                letters = set()
            letters.add(s[index])
        return k