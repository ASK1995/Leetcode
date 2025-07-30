from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = Counter()
        matches, smallest = 0, len(s) + 1
        left, res = 0, -1

        for index, letter in enumerate(s):
            count_s[letter] += 1
            if(count_s[letter] == count_t[letter]):
                matches += 1
            while(matches == len(count_t)):
                if(smallest > (index - left + 1)):
                    smallest = index - left + 1
                    res = left
                val = s[left]
                if(count_s[val] == count_t[val]):
                    matches -= 1
                left += 1
                count_s[val] -= 1
                if(count_s[val] == 0):
                    del count_s[val]

        if(res == -1):
            return ""
        return s[res:res + smallest]