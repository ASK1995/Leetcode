class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        last_row = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i, val in enumerate(row):
                last_row[i] = val + min(last_row[i], last_row[i + 1])

        return last_row[0]