class Solution:
    def sortString(self, s: str) -> str:
        count = [0] * 26
        res = ""
        for i in s:
            count[ord(i) - ord('a')] += 1

        while(len(res) < len(s)):
            for i in range(len(count)):
                if(count[i] >= 1):
                    res += chr(ord('a') + i)
                    count[i] -= 1
            for i in range(len(count) - 1, -1, -1):
                if(count[i] >= 1):
                    res += chr(ord('a') + i)
                    count[i] -= 1
        return res