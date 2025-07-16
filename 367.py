class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while(l <= r):
            m = (l + r)//2
            prod = m * m
            if(prod == num):
                return True
            elif(prod > num):
                r = m - 1
            else:
                l = m + 1
        return False