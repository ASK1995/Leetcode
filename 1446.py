class Solution:
    def maxPower(self, s: str) -> int:
        max_len, count = 0, 0

        for index in range(1, len(s)):
            letter = s[index]
            if(letter == s[index - 1]):
                count += 1
            else:
                count = 1
            max_len = max(max_len, count)
        return max_len