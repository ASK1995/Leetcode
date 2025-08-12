from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return 0
        res = [-1, -1]
        min_len = len(s) + 1
        l = 0

        count_t = Counter(t)
        to_match = len(count_t)
        matches = 0
        count_s = Counter()

        for index, letter in enumerate(s):
            count_s[letter] += 1
            if(count_s[letter] == count_t[letter]):
                matches += 1

            while(matches == to_match):
                size = index - l + 1
                if(size < min_len):
                    min_len = size
                    res = [l, index + 1]
                if(count_s[s[l]] == count_t[s[l]]):
                    matches -= 1
                count_s[s[l]] -= 1
                l += 1

        return s[res[0]: res[1]] if min_len != len(s) + 1 else ""