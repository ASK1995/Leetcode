class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        count = [0] * 10
        min_count = float('inf')

        while(n != 0):
            count[n % 10] += 1
            n //= 10
        res = float('inf')
        for i in range(10):
            if (count[i] != 0 and min_count > count[i]):
                min_count = count[i]
                res = i
        return res