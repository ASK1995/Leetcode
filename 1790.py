from collections import defaultdict

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count1, count2 = Counter(s1), Counter(s2)

        if(count1 != count2):
            return False

        diff = 0
        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                diff += 1

        return diff == 0 or diff == 2