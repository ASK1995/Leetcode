class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        res = 0

        for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if(index1 == index2):
                    continue
                if(nums[index1] + nums[index2] == target):
                    res += 1

        return res 