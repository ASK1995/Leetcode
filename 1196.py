class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        max_weight = 5000

        for index, value in enumerate(weight):
            if(max_weight - value >= 0):
                max_weight -= value
            else:
                return index

        return len(weight)