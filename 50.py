class Solution:
    def myPow(self, x: float, n: int) -> float:
        def divide_n_conquer(x, n):
            if(x == 0):
                return 0
            if(n == 0):
                return 1
            res = divide_n_conquer(x * x, n//2)
            return x * res if n % 2 != 0 else res
        res = divide_n_conquer(x, abs(n)) 
        if(n < 0):
            return 1/res
        return res