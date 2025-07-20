class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0

        while(i >= 0 and j >= 0):
            n1 = int(num1[i])
            n2 = int(num2[j])

            temp = n1 + n2 + carry
            carry = 0
            if(temp >= 10):
                carry = 1
            res += str(temp%10)

            i -= 1
            j -= 1

        while(i >= 0):
            n1 = int(num1[i])
            temp = n1 + carry
            carry = 0
            if(temp >= 10):
                carry = 1
            res += str(temp%10)

            i -= 1

        while(j >= 0):
            n2 = int(num2[j])
            temp = n2 + carry
            carry = 0
            if(temp >= 10):
                carry = 1
            res += str(temp%10)

            j -= 1

        if(carry == 1):
            res += str(1)

        return res[::-1]