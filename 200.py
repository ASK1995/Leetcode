class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None:
            return 0

        def dfs(i, j):
            if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1'):
                return

            grid[i][j] = '0'

            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dfs(i + x, j + y)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == '1'):
                    dfs(row, col)
                    count += 1

        return count