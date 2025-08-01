class Solution:
    def tribonacci(self, n: int) -> int:
        zero, one, two = 0, 1, 1

        if(n < 2):
            return n

        for i in range(2, n + 1):
            zero, one, two = one, two, zero + one + two

        return one