class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        min_distance = float('inf')

        for index, point in enumerate(points):
            i, j = point[0], point[1]
            if(not (i == x or j == y)):
                continue
            dist = abs(x - i) + abs(y - j)
            if(dist < min_distance):
                min_distance = dist
                res = index

        return res