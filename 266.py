from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odds = 0

        for key, value in count.items():
            if(value % 2 != 0):
                odds += 1
            if(odds > 1):
                return False

        return True