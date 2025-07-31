class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for index in range(0, len(nums), 2):
            even.append(nums[index])
        for index in range(1, len(nums), 2):
            odd.append(nums[index])

        even.sort()
        odd.sort(reverse=True)
        nums = []
        for index in range(len(odd)):
            nums.append(even[index])
            nums.append(odd[index])
        if(len(even) != len(odd)):
            nums.append(even[-1])
        return nums