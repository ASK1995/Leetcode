from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = Counter()
        max_count = 0

        for i in range(1, n + 1):
            digit_sum = 0
            while(i != 0):
                digit_sum += i % 10
                i //= 10

            group[digit_sum] += 1
            max_count = max(max_count, group[digit_sum]) 

        return sum(1 for value in group.values() if value == max_count)