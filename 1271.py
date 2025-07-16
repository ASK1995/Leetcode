class Solution:
    def toHexspeak(self, num: str) -> str:
        res = ""
        mapping = {0:'O', 1:'I', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        num = int(num)
        while(num != 0):
            digit = num % 16
            num //= 16
            if digit in mapping:
                res += str(mapping[digit])
            else:
                return "ERROR"
        return res[::-1]