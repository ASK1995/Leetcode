class Solution:
    def digitSum(self, num: int) -> int:
        total = 0

        while(num != 0):
            total += num % 10
            num //= 10

        return total

    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            if(self.digitSum(i) % 2 == 0):
                count += 1

        return count