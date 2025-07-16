class Solution:
    def decimalToBinary(self, decimal):
        res = ""
        while(decimal != 0):
            res += str(decimal % 2)
            decimal //= 2
        return res[::-1]

    def convertDateToBinary(self, date: str) -> str:
        date = date.split('-')
        year, month, day = [int(val) for val in date]
        res = "".join(self.decimalToBinary(year))
        res +=  '-' + "".join(self.decimalToBinary(month))
        res += '-' + "".join(self.decimalToBinary(day))
        return res