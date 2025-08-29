class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum, double_sum = 0, 0

        for num in nums:
            if(len(str(num)) == 2):
                double_sum += num % 10 + (num//10)*10
            elif(len(str(num)) == 1):
                single_sum += num % 10

        return single_sum != double_sum 