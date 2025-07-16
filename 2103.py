from collections import defaultdict

class Solution:
    def countPoints(self, rings: str) -> int:
        place = defaultdict(lambda:[])
        for index in range(0, len(rings), 2):
            color, ring = rings[index], rings[index + 1]
            place[int(ring)].append(color)
        res = 0
        for index in range(10):
            if(len(set(place[index])) == 3):
                print(place)
                res += 1
        return res