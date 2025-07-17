from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = defaultdict(lambda:0)
        start = 0
        longest = 0
        for index, letter in enumerate(s):
            count[letter] += 1
            while(len(count) > k):
                count[s[start]] -= 1
                if(count[s[start]] == 0):
                    del count[s[start]]
                start += 1
            longest = max(longest, index - start + 1)
        return longest