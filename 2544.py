class Solution:
    def alternateDigitSum(self, n: int) -> int:
        mul = 1
        num = str(n)
        res = 0

        for letter in num:
            val = mul * int(letter)
            res += val
            mul *= -1

        return res