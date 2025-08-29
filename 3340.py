class Solution:
    def isBalanced(self, num: str) -> bool:
        odd_sum, even_sum = 0, 0

        for index, val in enumerate(num):
            if(index % 2 == 0):
                even_sum += int(val)
            else:
                odd_sum += int(val)

        return odd_sum == even_sum