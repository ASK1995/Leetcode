from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq, min_val = 0, float('inf')

        for num in count.elements():
            if(num % 2 == 0):
                if(count[num] > max_freq):
                    max_freq = count[num]
                    min_val = num
                elif(count[num] == max_freq):
                    min_val = min(min_val, num)

        if(min_val == float('inf')):
            return -1
        return min_val