class Solution:
    def getLucky(self, s: str, k: int) -> int:
        transform = ""
        for letter in s:
            transform += str(ord(letter) - ord('a') + 1)
        while(k):
            total = 0
            for digit in transform:
                total += int(digit)
            transform = str(total)
            k -= 1
        return int(transform)