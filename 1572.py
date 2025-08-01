class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        total = 0

        for row in range(rows):
            total += mat[row][row]
        for row in range(rows):
            total += mat[row][rows - row - 1]

        if(rows % 2 != 0):
            total -= mat[rows//2][rows//2]

        return total