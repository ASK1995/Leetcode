class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows, columns = [0]*m, [0]*n
        res = 0

        for i in range(m):
            for j in range(n):
                if(mat[i][j] == 1):
                    rows[i] += 1
                    columns[j] += 1

        for i in range(m):
            for j in range(n):
                if(mat[i][j] == 1 and rows[i] == 1 and columns[j] == 1):
                    res += 1

        return res