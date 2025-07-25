class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res =[[0]*m for i in range(n)]
        for row in range(m):
            for column in range(n):
                res[column][row] = matrix[row][column]
        return res