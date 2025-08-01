class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            num = str(num)
            n = len(num)

            if(n % 2 != 0):
                continue
            l, r = 0, 0
            for j in range(n//2):
                l += int(num[j])
            for j in range(n//2, n):
                r += int(num[j])
            if(l == r):
                count += 1

        return count