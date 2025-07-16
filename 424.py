class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(lambda:0)
        start_index = 0
        longest = 0
        max_till_now = 0
        for index, letter in enumerate(s):
            count[letter] += 1
            max_till_now = max(max_till_now, count[letter])
            while(index - start_index + 1 - max_till_now) > k:
                count[s[start_index]] -= 1
                start_index += 1
            longest = max(longest, index - start_index + 1)
        return longest