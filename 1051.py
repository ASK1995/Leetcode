class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = [height for height in heights]
        expected.sort()
        res = 0

        for height, check in zip(heights, expected):
            if(height != check):
                res += 1
        return res