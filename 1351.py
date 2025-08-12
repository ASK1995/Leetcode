class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        negatives = 0

        for row in range(rows):
            col_l, col_r = 0, cols - 1
            res = col_r + 1
            while(col_l <= col_r):
                col_m = (col_l + col_r)//2
                if(grid[row][col_m] >= 0):
                    col_l = col_m + 1
                else:
                    res = col_m
                    col_r = col_m - 1
            negatives += cols - res

        return negatives