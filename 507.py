class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        i, total = 1, 0

        while (i * i < num):
            if(num % i == 0):
                total += i + num//i
            i += 1

        if i*i == num:
            total += i

        return total == num * 2