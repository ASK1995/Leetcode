class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        x, y = len(grid) - 1, 0
        negatives = 0

        while(x >= 0 and y < len(grid[0])):
            if(grid[x][y] < 0):
                negatives += len(grid[0]) - y
                x -= 1
            else:
                y += 1

        return negatives