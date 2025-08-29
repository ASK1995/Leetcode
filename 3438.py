class Solution:
    def findValidPair(self, s: str) -> str:
        count = [0]*10

        for digit in s:
            count[int(digit)] += 1

        for index, num in enumerate(s):
            if(index == len(s) - 1):
                return ""
            num1, num2 = int(num), int(s[index + 1])
            if(num1 != num2 and count[num1] == num1 and count[num2] == num2):
                return str(num1) + str(num2)

        return ""