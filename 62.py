class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if(i != 0 and j != 0):
                    res[i][j] = res[i - 1][j] + res[i][j - 1]

        return res[m - 1][n - 1]