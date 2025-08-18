from collections import defaultdict

class Solution:
    def romanToInt(self, s: str) -> int:
        maps = defaultdict()
        maps['I'] = 1
        maps['V'] = 5
        maps['X'] = 10
        maps['L'] = 50
        maps['C'] = 100
        maps['D'] = 500
        maps['M'] = 1000

        total = 0

        for index, letter in enumerate(s):
            if index + 1 < len(s) and maps[letter] < maps[s[index + 1]]:
                total -= maps[letter]
            else:
                total += maps[letter]
        
        return total