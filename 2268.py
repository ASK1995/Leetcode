from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = Counter(s)
        count = sorted(count.values(), key = lambda x : x, reverse = True)
        buttons, res = 0, 0
        mul = 1
        for value in count:
            res = res + (mul) * value
            buttons += 1
            if(buttons % 9 == 0):
                mul += 1
        return res