from collections import Counter

class Solution:
    def betterCompression(self, compressed: str) -> str:
        count = Counter()
        i, n = 0, len(compressed)

        while(i < n):
            j = i + 1
            x = 0

            while j < n and compressed[j].isdigit():
                x = x * 10 + int(compressed[j])
                j += 1

            letter, value = compressed[i], x
            count[letter] += value
            i = j

        res = ""

        for key in range(97, 123):
            if(count[chr(key)] != 0):
                res += chr(key) + str(count[chr(key)])

        return res