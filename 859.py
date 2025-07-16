from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)):
            return False
        count1, count2 = Counter(s), Counter(goal)
        if(count1 != count2):
            return False
        diff = 0
        for index in range(len(s)):
            if(s[index] != goal[index]):
                diff += 1
        return diff == 2 or (diff == 0 and any(val > 1 for val in count1.values()))