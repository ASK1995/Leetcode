class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_num, max_count = None, 0
        for index, num in enumerate(nums):
            if(max_count == 0):
                max_num, max_count = num, 1
            elif(num == max_num):
                max_count += 1
            else:
                max_count -= 1
                
        return max_num