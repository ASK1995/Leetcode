class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i, j = 0, 0
        res = ""
        ans = ""

        while(i < len(str1) and j < len(str2)):
            if(str1[i] == str2[j]):
                res += str1[i]
                i += 1
                j += 1
            else:
                break
            if(len(str1) % len(res) == 0 and len(str2) % len(res) == 0):
                if(res * (len(str1)//len(res)) == str1):
                    if(res * (len(str2)//len(res)) == str2):
                        ans = res

        return ans