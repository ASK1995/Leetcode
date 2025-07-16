class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
      
        prime = [True] * n
        res = 0
      
        for num in range(2, n):
            if prime[num]:
                res += 1
                for multiple in range(num * 2, n, num):
                    prime[multiple] = False

        return res