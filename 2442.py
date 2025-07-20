class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distincts = set()
        n = len(nums)

        for index in range(n):
            num = nums[index]
            distincts.add(num)
            distincts.add(int(str(num)[::-1]))

        return len(distincts)