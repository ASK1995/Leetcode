from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = defaultdict(lambda : 0)
        start = 0
        res = ""
        for index, letter in enumerate(s):
            res += letter
            if(index - start + 1 == 10):
                count[res] += 1
                res = res[1:]
                start += 1
        ans = []
        for key, value in count.items():
            if(value > 1):
                ans.append(key)
        return ans