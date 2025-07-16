class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = False
        if(n < 0):
            n *= -1
            neg = True
        def divide_n_conquer(x, n):
            if(x == 0):
                return 0
            if(n == 0):
                return 1
            res = divide_n_conquer(x * x, n//2)
            return x * res if n % 2 != 0 else res
        res = divide_n_conquer(x, n)
        if(neg):
            return 1/res
        return res