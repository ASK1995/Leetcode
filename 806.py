class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        res, current = 1, 0

        for letter in s:
            val = widths[ord(letter) - ord('a')]
            if(current + val > 100):
                current = val
                res += 1
            else:
                current += val

        return [res, current]