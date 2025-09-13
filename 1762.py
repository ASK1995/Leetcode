class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_h = heights[-1]
        res = [len(heights) - 1]
        for index in range(len(heights) - 2, -1, -1):
            if(heights[index] > max_h):
                res.append(index)
            max_h = max(max_h, heights[index])
        return res[::-1]