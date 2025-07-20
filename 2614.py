class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if(x == 2):
                return True
            elif(x % 2 == 0):
                return False
            for i in range(3, x, 2):
                if x % i == 0:
                    return False
                if(i * i > x):
                    break
            return True

        n = len(nums)
        max_prime = 0
        for i, row in enumerate(nums):
            if is_prime(row[i]):
                max_prime = max(max_prime, row[i])
            if is_prime(row[n - i - 1]):
                max_prime = max(max_prime, row[n - i - 1])
        return max_prime