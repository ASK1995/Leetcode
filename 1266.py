class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x, y = points[0][0], points[0][1]

        for point in points:
            res += max(abs(x - point[0]), abs(y - point[1]))
            x, y = point[0], point[1]

        return res