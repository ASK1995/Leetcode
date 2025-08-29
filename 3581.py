from collections import defaultdict
from collections import Counter

class Solution:
    def countOddLetters(self, n: int) -> int:
        s = ""
        converter = {0:"zero", 1:"one", 2:"two", 3:"three",
        4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
        for letter in str(n):
            s += converter[int(letter)]

        count = Counter(s)
        return sum(1 for key, value in count.items() if value % 2 != 0)