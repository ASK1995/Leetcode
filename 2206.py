class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odds = set()

        for num in nums:
            if num in odds:
                odds.discard(num)
            else:
                odds.add(num)
        return len(odds) == 0