class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        swaps = 0

        while(swaps != 2):
            swaps = 0
            for index, value in enumerate(nums):
                if(value != index):
                    swaps += 1
                nums[index], nums[value] = nums[value], nums[index]

        return [nums[-1], nums[-2]]