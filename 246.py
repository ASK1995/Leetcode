class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        l, r = 0, len(num) - 1
        while(l <= r):
            left, right = int(num[l]), int(num[r])
            if(left in [2, 3, 4, 5, 7]):
                return False
            elif(left in [0, 1, 8]):
                left = left
            elif left == 6:
                left = 9
            else:
                left = 6
            if(left != right):
                return False
            l, r = l + 1, r - 1
        return True