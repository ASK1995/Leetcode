class Solution:
    def digitCount(self, num: str) -> bool:
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for digit in num:
            val = ord(digit) - ord('0')
            count[val] += 1

        for index, digit in enumerate(num):
            x = int(digit)
            y = count[index]
            if(x != y):
                return False

        return True