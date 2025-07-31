class Solution:
    def ones(self, num):
        res = 0

        while(num != 0):
            if(num % 2 != 0):
                res += 1
            num //= 2

        return res

    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda x: (self.ones(x), x))
        return arr