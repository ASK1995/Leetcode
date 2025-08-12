from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = defaultdict(lambda : 0)
        i = 0

        while i + 9 < len(s):
            res = s[i : i + 10]
            count[res] += 1
            i += 1

        ans = [key for key in count.keys() if count[key] > 1]
        return ans