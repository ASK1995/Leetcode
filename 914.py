from collections import Counter
from functools import reduce
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck).values()
        return reduce(gcd, count) >= 2