class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        left = 0
        longest = 0

        for index, letter in enumerate(s):
            while(letter in letters):
                letters.discard(s[left])
                left += 1
            letters.add(letter)
            longest = max(longest, index - left + 1)

        return longest