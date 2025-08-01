class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elements, digits = 0, 0

        for num in nums:
            elements += num
            while(num != 0):
                digits += num % 10
                num //= 10

        return elements - digits