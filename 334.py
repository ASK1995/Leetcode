class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b, c = float('inf'), float('inf'), float('inf')

        for num in nums:
            if(num <= a):
                a = num
            elif(num <= b):
                b = num
            elif(num <= c):
                return True
        return False