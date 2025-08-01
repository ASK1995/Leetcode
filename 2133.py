class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)):
            s = set()
            for column in range(len(matrix)):
                s.add(matrix[row][column])
            if(len(s) != len(matrix)):
                return False

        for column in range(len(matrix)):
            s = set()
            for row in range(len(matrix)):
                s.add(matrix[row][column])
            if(len(s) != len(matrix)):
                return False

        return True