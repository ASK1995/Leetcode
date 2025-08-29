class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        res = -1

        while(l <= r):
            m = (l + r)//2
            if(arr[m] == m):
                res = m
                r = m - 1
            elif(arr[m] > m):
                r = m - 1
            else:
                l = m + 1

        return res if res != -1 else -1