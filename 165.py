class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        while(len(version1) < len(version2)):
            version1.append('0')
        while(len(version2) < len(version1)):
            version2.append('0')

        i = 0
        while(i < len(version1) and i < len(version2)):
            num1, num2 = int(version1[i]), int(version2[i])
            if(num1 < num2):
                return -1
            elif(num1 > num2):
                return 1
            i += 1
        return 0