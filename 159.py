from collections import Counter

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count = Counter()
        start = 0
        longest = 0
        for index, letter in enumerate(s):
            count[letter] += 1
            while(len(count) > 2):
                letter = s[start]
                count[letter] -= 1
                if(count[letter] == 0):
                    del count[letter]
                start += 1
            longest = max(longest, index - start + 1)
        return longest