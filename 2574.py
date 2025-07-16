class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = [], []
        curr = 0
        for num in nums:
            leftSum.append(curr)
            curr += num
        curr = 0
        for num in nums[::-1]:
            rightSum.append(curr)
            curr += num
        rightSum = rightSum[::-1]
        res = []
        for i in range(len(nums)):
            res.append(abs(leftSum[i] - rightSum[i]))
        return res