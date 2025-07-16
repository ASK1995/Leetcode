class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        l1 = queryIP.split('.')
        l2 = queryIP.split(':')
        v4 = True
        if(len(l1) > 1):
            v4 = True
        elif(len(l2) > 1):
            v4 = False
        if(v4):
            if(len(l1) != 4):
                return "Neither"
            for num in l1:
                if not num.isdigit() or not(0 <= int(num) <= 255) or (num[0] == "0" and len(num) > 1):
                    return "Neither"
            return "IPv4"
        else:
            if(len(l2) != 8):
                return "Neither"
            for num in l2:
                if(not num or len(num) > 4):
                    return "Neither"
                if(not all(letter in '0123456789abcdefABCDEF' for letter in num)):
                    return "Neither"
            return "IPv6"