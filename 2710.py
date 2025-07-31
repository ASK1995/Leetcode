class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        start, end = 0, len(num) - 1

        while(start < len(num)):
            if(num[start] != '0'):
                break

            start += 1

        while(end >= 0):
            if(num[end] != '0'):
                break

            end -= 1

        return num[start:end + 1]